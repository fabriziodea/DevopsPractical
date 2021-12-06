# DevOps Core Practical Project

## Contents:
* Project Brief 
* The Application
* Requests
* Database Table Structure
* Project Tracking
* Risk Assessment
* Version Control
* Containerisation and Orchestration
* Reverse Proxy
* Unit Testing
* CI Server
* Dockerhub and Nexus
* Ansible
* Cloud Provider

## Project Brief
This project required the creation of a service-orientated architecture for an application composed of at least 4 services that work together.
Service 1 renders the Jinja2 templates and it is responsible to communicate with the other 3 services.
It is also required to persist data to a SQL database.
Service 2 and 3 generate random objects.
Service 4 create and object based on the results of service 2 and 3.
It is also required to use:
* A project tracking software allowing agile management.
* A version control system using the Feature-Branch model.
* A CI server to build and deploy the application.
* A cloud based provider to provision the virtual machines the application will run on.
* Containerisation and orchestration tools.
* An Ansible playbook to provide the environment the application needs to run.
* A reverse proxy to be accessible to the user

## The Application
My application is a race simulator, it generate 8 random names for the contenders and it randomly picks a winner.
* Service 1 is the frontend, it provides the Jinja2 templates and communicates with the other 3 services.
* Service 2 generates a random name for a single contender
* Service 3 randomly picks the race winner
* Service 4 is the race builder it takes the random values and it generates a json file with all the information to run a race, 8 names and a winner.
* DB is the database container where the MySQL database saves the winner name for each race, a volume is mounted to the DB container

## Requests
Service 1 sends http get requests to Service 2 and 3 to retrieve the random values, then it sends a http post request to Service 4 to build a single race as shown below:
![Services](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/Services.png)

## Database Table Structure
The database saves the name of the winner for each race:
![Database](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/Database.png)

## Project Tracking
I chose Jira as project tracking tool, I created Epics to indicate the main areas I needed to work on, I broke down the epics in user stories and I subsequently added user stories to sprints.
This was very useful to have a clear views of the issues that needed attention and to prioritise appropriately the most urgent tasks.
Here I show the Roadmap, Sprint board and Backlog when the project was ongoing:
![Backlog](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/backlog.png)
![Board](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/Board2.png)
![Roadmap](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/Roadmap.png)

## Risk Assessment
A risk assessment was created in order to monitor any potential risks that could jeopardise the project.
![Risk Assessment](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/RiskAssessment.png)

## Version Control
I chose Git as a version control system. I made sure to create different branches and work on a dev branch everytime i was adding a new feature merging to the main branch when all known issues were solved. I also linked Github to Jira and i used smart commits to automatically update the Jira Board everytime a commit was modifying the state of the user stories in a sprint.
Here there is the repository during the project and the branch diagram:
![GitRepo](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/Git1.png)
![Branches](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/Branches.png)

## Containerisation and Orchestration
This is a distributed application where the services runs in separate containers and the containers are replicated on 2 Vms.
This architecture improves the resilience of the application in case of failure.
Docker swarm is used to orchestrate and manage the containers replicas across the 2 Vms.

## Reverse Proxy
The ansible playbook sets up a VM as the reverse proxy using Nginx.
This machine is reachable on port 80, it doesn't host the application but it forwards the traffic to 2 VMS hosting the application containers as shown in the diagram below.
![NGINX](https://github.com/fabriziodea/DevopsPractical/blob/main/Images/Nginx.png)

## Unit Testing
Unit testing for this project was carried out with Pytest.
Each function within every route for every service is tested to verify the application handles and returns data as expected.
Unit tests are triggered automatically with the Webhooks through Github after each push to the repository.
All tests covered 100% and passed.

## CI Server
The CI Server is Jenkins, it creates a new build triggered via webhook fron Github after every commit. Jenkins is responsible of a number of tasks:
* It runs automated tests for each service.
* It builds images for each service and push them to Dockerhub, in order to make them available to all the VMs requiring the service images.
* It transfer the docker-compose.yaml file to the Swarm manager node,
* It runs the Ansible playbook, where it provisions the software and the dependencies required to each VMs involved with the application.
* Once all the VMs have the required software and the images are available on Dockerhub it deploys the application.

## Dockerhub and Nexus
The services images are available on a public repository at https://hub.docker.com/.
Since there was no requirement for confidentiality or high performance Dockerhub was my choice as image repository.
If I had the need to access the repository quicker a solution could be Nexus. Nexus is a repository manager that can be installed on a local server, cutting down access time and improving confidentiality since the repository would be private.
It also has a system to cache commonly used images to speed up deployment.

## Ansible
Ansible was used as software provisioning and configuration management tool.
The playbook installs Docker on the VMS hosting the containers, initiate Docker Swarm on the manager node and it passes the token to worker node to join the swarm. It also install nginx on the VM acting as a load balancer
Finally it deploys the application running the Docker stack deploy command on the Swarm manager node.

## Cloud provider
Google cloud platform is the cloud provider i used for this project.
Moving the application on the cloud offers many advantages.
It allows greater scalability by giving the possibility to add more virtual machines and more replicas.
It makes the application more resistant in case of failure.
It allows automatic updates with no or little down time.
