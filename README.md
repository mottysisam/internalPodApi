# pod-info
1. minikube start
2. minikube addons enable ingress
3. kubectl create -f manifests/pod-read-role.yaml manifests/deployment.yaml manifests/ingress.yaml
4. minikube tunnel
5. generate ssl cert/key
** openssl genrsa -out s.key 2048
** openssl req -new -key s.key -out s.csr -subj "/CN=example.com"
** openssl x509 -req -days 365 -in s.csr -signkey s.key -out s.crt
6. kubectl create secret tls myssl --cert s.crt --key s.key
7. add example.com to /etc/hosts (127.0.0.1 example.com)
8. kubectl expose deployment pod-info-app --type=NodePort --port=5000

