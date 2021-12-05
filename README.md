=-=-=-=-=-=-=-=-=-=-=-=-=-
## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)

![Jira Board1](https://github.com/fabriziodea/fabproj1/blob/master/Images/Jira%20Board.png)
=-=-=-=-=-=-=-=-=-=-=-=-=-
# DevOps Core Practical Project


## Contents:
* Project Brief 
* The Application
* Requests
* Database Table Structure



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
!SERVICESXXXXXXX
## Database Table Structure
The database saves the name of the winner for each race:
!DATABASEXXXX

## Project Tracking
I chose Jira as project tracking tool, I created Epics to indicate the main areas I needed to work on, I broke down the epics in user stories and I subsequently added user stories to sprints.
This was very useful to have a clear views of the issues that needed attention and to prioritise appropriately the most urgent tasks.
Here I show the Roadmap, Sprint board and Backlog when the project was ongoing:
!BacklogXXX
!Board XXX
!Roadmap XXX

## Risk Assessment
A risk assessment was created in order to monitor and plan for any potential risks that could jeopardise the project.
!RiskassessmentXXX

## Version Control
I chose Git as a version control system. I made sure to create different branches and work on a dev branch everytime i was adding a new feature. Merging to the main branch when all known issues were solved. I also linked Github to Jira and i used smart commits to automatically update the Jira Board everytime a commit was modifying the state of the user stories in a sprint.
Here there is the repository during the project and the branch diagram:
!GitRepoxxx
!GitBranchesxxx










