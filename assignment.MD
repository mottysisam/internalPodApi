# ASSIGNMENT

1. Create a container (use any programming language you feel comfortable with) that can
access k8s API to expose an endpoint (e.g., http://example.com:8080/info) that returns
pod information (e.g., what you’d get when using kubectl get pods -n namespace
pod-name -o json). See sample output on the next page.

2. Build and push the container to any free docker repo for the next steps.

3. Install a k3s cluster with one master node (you can install it from the binary or k3sup).

4. Deploy 2 deployments (Yaml or Helm) of the image you built and pushed in step 2

5. Create a single ingress for both apps with a path for each one.
Example: if we go to example.com/a we reach the first app and example.com/b will
reach the second app).
** You can use any ingress controller you know (nginx, traefik etc…)

6. Connect a certificate to the ingress that when reached from browser it will not show the
kubernetes fake certificate but the created certificate (you can use self signed certificate
or install cert manager to do it).
