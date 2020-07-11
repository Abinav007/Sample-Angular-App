+ Create docker image using 

  docker build -t <image tag> .
  docker push <image tag> 
 
+ Run using minikube

  1.Navigate to the directory containing deploy.yml
  
  2.Use the following command to create the service and deployment using the yml file :
  
    kubectl apply -f deploy.yml

  3.Create service with type LoadBalancer , command :
  
    kubectl expose deployment fetch-deployment --type=LoadBalancer --name=fetch-lb

  4. Use the following command to assign the pending external ip :
   
    minikube tunnel

  5.Then you will be able to view the output on the external ip with the port we specified in the yml file 
  
  6. Use the following command to view dashboard
  
    minikube dashboard
