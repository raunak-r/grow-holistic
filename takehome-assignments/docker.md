# Dockerization
This doc has 2 tasks

## Task 1 - Docker
```
Create a flask app with an endpoint /live which will return {"status": "Running"} when http://localhost:5000/live is executed on chrome/postman.
Instead of running the server using the "flask --app appname run" terminal command,
write a docker file and run it.
```

## Task 2 - Docker Compose
```
Create a flask app with an endpoint /user/{userId} which will return {"data": user_data}
inside the app
- create a user model with
  - first_name
  - phone
- save the db schema in postgres

Instead of running the server using the "flask --app appname run" terminal command,
and running postgres on your system
write a docker-compose file to run both postgres and flask.
```

## Task 3 - Docker Swarm
```
Start a container of docker and manage it using docker swarm
```

## Task 4 - Kubernetes
```
Instead of docker swarm, use kubernetes.
```
