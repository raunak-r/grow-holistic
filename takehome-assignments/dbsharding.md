## Task
Read the topic on - How Figma Scaled their Database Stack - https://blog.quastor.org/p/figma-scaled-databases-100x

## Project
```
1. Create a postgres table - with User column
2. Create a django project with
  - model definition of table
  - class Based view with GET, POST, PUT, DELETE
  - service file with functions to work on the data.

3. Add 3 urls 
  - /users/normal/
  - /users/caching/
  - /users/sharding/
  The task will be to implement 3 different versions of the api, one with a normal retrieval of data from db, second to use an intermediate caching layer, and third to implement sharding.

4. The /normal/ api will be a direct django query orm implementation on the model User.
5. in the /caching/ api use something like django cache-ops library to implement caching.
6. in the /sharding/ api
  - first create a shard key
  - implement a db router
  - implement all the rest apis for the same.
```

## Deliverables
```
a postgresql db schema, and a django codebase with the above mentioned files.
```
