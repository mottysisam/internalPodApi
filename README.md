# Internal Pod API
- Quick Install - ✨Magic ✨

## Minikube & Ingress enabled & Tunnel
```
1. minikube start
2. minikube addons enable ingress
3. minikube tunnel
```

## Patch manifests
```
kubectl create: 
- manifests/pod-read-role.yaml 
- manifests/deployment.yaml 
- manifests/ingress.yaml
```
## SSL Certs
```
** openssl genrsa -out s.key 2048
** openssl req -new -key s.key -out s.csr -subj "/CN=example.com"
** openssl x509 -req -days 365 -in s.csr -signkey s.key -out s.crt
- kubectl create secret tls myssl --cert s.crt --key s.key
```

## Make example.com available to localhost 
```
add example.com to /etc/hosts (127.0.0.1 example.com)
```


### THE END
