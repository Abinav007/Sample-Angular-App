# SampleAngular

This project was generated with [Angular CLI] version 9.1.7.
## Clone the project using this Link :
   1. Command to clone the project is git clone https://github.com/Abinav007/Sample-Angular-App.git .
   2. Install Node.js in your Local System.
   3. After successfully cloning te project , give npm install to download to get node_modules Folder.
## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.


## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
# Angular Application Overview
 
 ng denotes Angular Application.
 
 g denotes generate.
 
 ## Component Creation :
 
  1. Open Terminal or Command Prompt , Give the following Command : ng g c (component-name). (c denotes component)
  2. It creates folder named (component-name) with three files :
  		1. (component-name).component.ts
  		2. (component-name).component.html
  		3. (component-name).component.css
  
  ## Service Creation:
  
  1. Open Terminal or Command Prompt , Give the command as : ng g s (service-name). (s denotes service)
  2. It creates two files in the app folder :
  		1. (service-name).service.ts
  		2. (service-name).spec.ts

-----------------------------------------------------------------------------------------------------------

deployment.yaml:

Open a New Terminal Window : 

1. Run the command : minikube tunnel

Check the service name is specified in <your-service-name>

Try the below the Steps , and Check your <your-service-name> specified in minikube tunnel window. 

Need to try the below command , to check Service works fine in the CLI :

   kubectl expose deployments <my-deployment-name> --type=LoadBalancer --name=<my-service-name>

After Service created successfully.

Then, Give the below command :

   minikube service <my-service-name>(Automatically opens in browser) 

If the above command works , Service and minikube working is fine.

Need to Check our Service file specification.

Step 1: 
By default , the Service type is ClusterIP. So , you cant able to view in the browser.

So , Need to specify Service type as ## Loadbalancer.

then , given the below command :

   minikube service <your-service-name>

(Browser gets Opens Automatically)

Check the <your-service-name> specified in minikube tunnel window.

If success, Leave the below steps. or else proceed the below steps.

Step 2:
 
Specify the nodePort as "nodePort: <30000 - 32767>" in your yaml File

Try any number between 30000 - 32767 to nodePort.

then , given the below command :

   minikube service <your-service-name>

(Browser opens automatically)

The above two steps works for me.
