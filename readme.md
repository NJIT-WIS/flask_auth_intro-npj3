# Project Status

Name: Nava Praharsha
UCID: npj3@njit.edu

[![Production Workflow]() <-Put your own badge code here.

[Production Deployment]()

# User Authentication, authorization, Validation, and Database Introduction

In this unit, I am giving you a complete application that demonstrates authentication, authorization, validation, and
interacting with an SQL database using the library sqlalchemy. You should investigate this code and learn to navigate
the directory structure, start the application, manage it on your own computer, and deploy it to Heroku. In the unit video I
will show you how to do it manually and using the automation tools that PyCharm pro provides. You can probably get by
with Pycharm community; however, some things will not work for you that I do in this unit.

## Unit Video
* [Unit Video - Here](https://youtu.be/w_-LSC045ac)

The first 90 minutes or so is web security and then last 30 minutes are going over the applications.  YOu might want to watch this in two sessions.

You need to write tests for the following functionality in the [task1_tests.py file](tests/task1_test.py). You can find
examples of similar tests in the [auth_test.py file](tests/auth_test.py)

1. Test to see you get the correct error message when trying to login with a bad username
2. Test that you are not allowed to access the dashboard without being logged in.  The app should return a 302 access denied status code
3. Fix all the pylint errors by correcting ones that you think can be fixed like doc strings, while others can be disabled like the missing member error

### Submission Instructions
1. Set up the application as you did before, you can copy your prod.yml file from the previous assignment.  You will need 
   to add the heroku API key, docker username, docker password secrets to this repository
2. Add your name to the top of the readme, add the link to your deployed app, and add the badge code as you did before.

### Docker Commands
1. docker ps <- lists running containers
2. docker kill <container id>  kills the container, you get the container ID from docker PS
   * Example: docker kill cf373e38ae66
3. docker compose up --build <- builds the app locally
4. docker exec -it <containerID> /bin/bash    <- Logs into the running container
   * Example: docker exec -it cf373e38ae66 /bin/bash

Note:  You really want to login to the container to run pytest but you can also run it locally as long as you create the virtual environment and do the pip install requirements

### Required Readings

1. [Authentication vs Authorization](https://medium.com/plain-and-simple/identification-vs-authentication-vs-authorization-e1f03a0ca885)
2. [Understanding HTTPS](https://johnopdenakker.com/understanding-https/)
3. [Understanding SSL](https://blog.hubspot.com/marketing/what-is-ssl)
4. [Understanding RSA Encrpytion (basis of SSL)](https://comodosslstore.com/resources/what-is-an-rsa-algorithm-in-cryptography/)
5. [Understanding Hashing and Bcrypt](https://clerk.dev/blog/bcrypt-hashing-authentication-encryption)
6. [Types of Authentication used with Web Applications](https://medium.com/@vivekmadurai/different-ways-to-authenticate-a-web-application-e8f3875c254a)
7. [More about CSRF TOkens - easier to understand](https://brightsec.com/blog/csrf-token/)
8. [Same Origin Secutity Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)
9. [Understanding Sessions and Problems with Sessions](https://machinesaredigging.com/2013/10/29/how-does-a-web-session-work/)
10. [Understanding CORS and Same Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

### Optional Readings

1. [CSRF - Understanding a major web security issue - more complete](https://owasp.org/www-community/attacks/csrf)

# Project Setup

## Setting up CI/CD

The result of this will be that when you create a pull request to merge a branch to master, it will deploy to your
heroku development app/dyno and when you merge or push to master on github, it will deploy the app to the production
heroku app/dyno.

### Instructions

1. Create an account with Heroku, create an app for production and an app for development
2. Create a new repo in Docker hub

#### Setup Docker and Heroku Credentials In the Repository Settings under Action -> Secret

3. In your newly created Github repository, add new repository secrets for DOCKER_USERNAME, DOCKER_PASSWORD,
   HEROKU_API_KEY (Values are DOCKER_USERNAME: your docker hub username; DOCKER_PASSWORD: your docker hub password;
   HEROKU_API_KEY: API key from the heroku app)

### GitHub Notes:  Set the action secrets repository in: -> settings -> actions -> secrets

### Heroku Notes: Get the heroku API key from account in: -> applications -> create authorization button

#### Change GitHub Actions Workflows for Prod

4. Change line 42 to have your docker repo address in: .github/workflows/prod.yml
5. change lines 58 to have your heroku app name in: .github/workflows/prod.yml
6. change line 59 to have your heroku email in: .github/workflows/prod.yml
7. Push code to your local repo and check for any errors and fix any errors that appear when the workflow is running.
   You can check the workflow in the
   actions.

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest

### Future Notes and Resources

* https://flask-user.readthedocs.io/en/latest/basic_app.html
* https://hackersandslackers.com/flask-application-factory/
* https://suryasankar.medium.com/a-basic-app-factory-pattern-for-production-ready-websites-using-flask-and-sqlalchemy-dbb891cdf69f
* https://develie.hashnode.dev/exploring-flask-sqlalchemy-queries
* https://wtforms.readthedocs.io/en/3.0.x/
* https://bootstrap-flask.readthedocs.io/en/stable/
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/
