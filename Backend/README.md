# To create docker image

- minikube start
- docker build -t <image-name>:<tag-name> .
- kubectl apply -f deploy.yml
- kubectl expose deployment fetch-deployment --type=LoadBalancer --name=fetch-lb
- kubectl get services
(If external IP is not assigned, run minikube tunnel on different command line)