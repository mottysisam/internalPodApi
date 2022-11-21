import sys
import logging
import subprocess
import json
import os
import requests


logger = logging.getLogger('pod_info')
logger.setLevel(logging.INFO)

# Env Consts
POD_NAMESPACE = os.environ.get("POD_NAMESPACE", "default")
POD_NAME = os.environ.get("POD_NAME", os.uname()[1])
KUBERNETES_SERVICE_HOST = os.environ.get("KUBERNETES_SERVICE_HOST", "172.30.0.1")
KUBERNETES_PORT_443_TCP_PORT = os.environ.get("KUBERNETES_PORT_443_TCP_PORT", "443")


def api_get(url, token):
    try:
        head = {'Authorization': 'Bearer {}'.format(token)}
        logger.info(f"Trying to GET with URL: {url} and token: {token}...")
        response = requests.get(url, headers=head, timeout=10, verify=False)
        return response.content
    except Exception as exc:
        err_message = f"GET request failed: {exc}"
        logger.exception(err_message)
        return err_message


def get_token():
    command = "cat /var/run/secrets/kubernetes.io/serviceaccount/token"
    output = run_shell_cmd(command)
    return output


def run_shell_cmd(command):
    try:
        output = subprocess.getoutput(command)
        return output
    except:
        err_message = f"Error: Could not run command: {command}"
        logger.error(err_message)
        return err_message


def get_pod_info_kubectl(pod_namespace, pod_name):
    try:
        command = f"kubectl get pods -n {pod_namespace} {pod_name} -o json"
        json_str = subprocess.getoutput(command)
        return json.loads(json_str)
    except:
        err_message = f"Error: Could not get pod info in Namespace: {pod_namespace} with Pod Name: ${pod_name}"
        logger.error(err_message)
        return {
            'error': {'message': [err_message]}
        }


def get_pod_info_curl(pod_namespace, pod_name):
    try:
        token = get_token()
        url = f"https://{KUBERNETES_SERVICE_HOST}:{KUBERNETES_PORT_443_TCP_PORT}/api/v1/namespaces/{pod_namespace}/pods/{pod_name}"
        output = api_get(url, token)
        return json.loads(output)
    except:
        err_message = f"Could not get pod info in Namespace: {pod_namespace} with Pod Name: ${pod_name} - {output}"
        logger.exception(err_message)
        return {
            'error': {'message': [err_message]}
        }


def main():
    pod_info = get_pod_info_curl(POD_NAMESPACE, POD_NAME)
    print(pod_info)
    return pod_info


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s")
    sys.exit(main())
  



