# Caching & Sharding
Read the topic on - How Figma Scaled their Database Stack - https://blog.quastor.org/p/figma-scaled-databases-100x

Your task is to create a Flask project that demonstrates different techniques for data retrieval and manipulation inspired by how Figma scaled their database stack.

## Project Requirements:
PostgreSQL Setup:
```
Create a PostgreSQL table with a User column.
```

Flask Project:
```
Set up a Flask project with the following:
Model definition for the User table.
Class-based views to handle GET, POST, PUT, DELETE requests.
Service file with functions to work on the data.
```

URLs and Views:
```
Implement three different versions of the API with the following URLs:
/users/normal/
/users/caching/
/users/sharding/
```

API Implementations:
```
/users/normal/: Implement a direct SQLAlchemy query on the User model.
/users/caching/: Use a caching mechanism (e.g., flask-caching) to implement caching.
/users/sharding/: Implement database sharding.
```

```
Create a shard key.
Implement a database router.
Implement all REST APIs (GET, POST, PUT, DELETE) for the sharding approach.
```

## Deliverables:
```
A PostgreSQL database schema.
A Flask codebase with the following components:
Model definition for User.
Class-based views for the API endpoints.
Service file with data manipulation functions.
URL configurations for /users/normal/, /users/caching/, and /users/sharding/.
Implementation of caching and sharding mechanisms as specified.
```

## Follow-up Questions:
```
How would you ensure data consistency across different shards?
What strategies would you use to handle cache invalidation?
How would you monitor the performance of each retrieval method (normal, caching, sharding)?
How would you handle a high volume of concurrent requests to ensure the system remains responsive?
```
