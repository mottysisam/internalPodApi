# Internal Pod API
- Quick Install - ✨Magic ✨

# 1. Choose a Kube System (k3s / minikube) 

## Minikube & Ingress enabled & Tunnel
```
1. minikube start
2. minikube addons enable ingress
3. minikube tunnel
```

## k3s
```
1. wget https://github.com/k3s-io/k3s/releases/download/v1.23.5%2Bk3s1/k3s
2. chmod +x k3s
3. sudo ./k3s server &&
4. sudo ./k3s kubectl get nodes
```

# 2. Patch manifests
```
kubectl create: 
- manifests/pod-read-role.yaml 
- manifests/deployment.yaml 
- manifests/ingress.yaml
```

# 3. SSL Certs (Use certs in auth dir or create your own certs) 
```
** openssl genrsa -out s.key 2048
** openssl req -new -key s.key -out s.csr -subj "/CN=example.com"
** openssl x509 -req -days 365 -in s.csr -signkey s.key -out s.crt
- kubectl create secret tls myssl --cert s.crt --key s.key
```

# 4. Make example.com available to localhost 
```
add example.com to /etc/hosts (127.0.0.1 example.com)
```

# 4. Check your running service
```
- curl -k https://example.com/a 
- curl -k https://example.com/b 
```

### THE END
