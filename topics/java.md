# Java
Refer - https://www.geeksforgeeks.org/30-days-of-sql-from-basic-to-advanced-level/

Before you start, save all these scripts under the folder name 'java-notes' on your personal git account.

## Installations
```
1. Local Installation
Download intellij Idea Community.

2. Java Basics - A few questions to refresh python memory.
- [Question Bank Link](https://www.w3resource.com/java-exercises/ - first 5 question of each topic mentioned below
```

## Baby Basics - Java
```
Basic Exercises Part-I [ 150 Exercises with Solution ]
Basic Exercises Part-II [ 99 Exercises with Solution ]
Data Types Exercises [ 15 Exercises with Solution ]
Conditional Statement Exercises [ 32 Exercises with Solution ]
Array [ 74 Exercises with Solution ]
String [ 107 Exercises with Solution ]
Date Time [ 44 Exercises with Solution ]
Methods [ 16 Exercises with Solution ]
Numbers [ 28 Exercises with Solution ]
Input-Output-File-System [18 Exercises with Solution ]
Collection [ 126 Exercises with Solution ]
Math [ 27 Exercises with Solution ]
Sorting [ 19 Exercises with Solution ]
Search [ 7 Exercises with Solution ]
```

## Basics

Springboot
```
Make a git repo by the name of springboot-demo
On starting the below project, commit the whole project, after each video.
A total of atleast 15 commits should be there after the videos end.
```

https://www.youtube.com/watch?v=35EQXmHKZYs&ab_channel=Telusko

```
Introduction - 00:00
1. What is Spring ? – 00:05
2. Dependency Injection? – 05:34
3. Spring Tool Suite | Spring Boot IDE – 13:40
4. Spring, Autowire, Dependency Injection – 22:17
5. Web App using Spring Boot – 40:39
6. Application Properties File – 55:33
7. Accepting Client Data – 01:00:11
8. ModelAndView – 01:08:51
9. Model Object – 01:16:12
10. JPA | MVC | H2 Example – 01:20:29
11. JPA | MVC | H2 Example Part 2 – 01:35:29
12. Data JPA | MVC | H2 | Query Methods Example  – 01:45:12
13. Data JPA | MVC | H2 | REST Example – 01:54:43
14. Data JPA | MVC | H2 | REST Example – 02:02:22
15. Postman | Data JPA | MVC | H2 | REST Example – 02:06:55
16. Content Negotiation | Data JPA | MVC | H2 | REST  – 02:11:29
17. Spring Boot | MVC | REST Post Example  – 2:19:36
18. Spring Boot | MVC | REST PUT DELETE Example – 02:27:35
19. Spring Boot Data REST Example – 02:36:30
```


```
Refer https://www.baeldung.com/rest-with-spring-series
Bootstrapping a Web Application  
Building a REST API  
The Spring @Controller and @RestController Annotations  
Error Handling for REST (popular)
Entity To DTO Conversion for a Spring REST API
Spring’s RequestBody and ResponseBody Annotations  
How to Read HTTP Headers in Spring REST Controllers  
Using Spring @ResponseStatus to Set HTTP Status Code  
Using Spring ResponseEntity to Manipulate the HTTP Response  

Properties with Spring and Spring Boot (popular)
Guide to @ConfigurationProperties in Spring Boot
Automatic Property Expansion with Spring Boot
Using application.yml vs application.properties in Spring Boot


How to Change the Default Port in Spring Boot
Spring Boot Change Context Path
Spring Boot: Customize Whitelabel Error Page
```


```
Refer https://medium.com/javarevisited/13-topics-you-should-prepare-for-your-next-spring-boot-interview-5f2993a04ff5
1. Container, Dependency, and IOC
2. Spring Bean Lifecycle
3. Aspect-Oriented Programming (AOP)
4. Spring MVC
5. Spring Boot Basics
6. Spring Boot Auto Configuration
7. Spring Boot Starter Dependency
8. Spring Boot Actuator
```

## Intermediate
```
Spring Security
Minor Project 2 : Developing a Web App (Micro-service) using Spring Boot + Hibernate+ MySQL + RESTful APIs + OAuth 2 + Security
Redis, Kafka
Kafka with Spring Boot
Redis with Spring Boot
```

```
Refer https://www.baeldung.com/spring-boot
Spring Boot - DevOps Tools
Dockerizing a Spring Boot Application
Creating Docker Images with Spring Boot
A Guide to Spring Boot Admin
Overview of Spring-Boot Dev Tools
Introduction to Spring Boot CLI
Spring Boot Application as a Service
Running Spring Boot Applications With Minikube
```
## Advanced
```
No Limits.
```

## Archives
```
Make a git repo by the name of java-demo
For each question-type, make a corresponding file for that, having 5 answers/questions in each file.
and save the same in git.
A total of 14 commits must be there, in a clean and presentable manner with each commit showing the answers of one topic.

For each topic, you've to make a Pull Request, and make a commit for each of the 5 answers solved for the same.
Hint -> Use the branch checkout, and merge features to do this.
```

## Springboot
```
- Define @entity class
    - user table - design a table with created_time, updated_time, name, phone number, city, isDeleted
        - @uniqueConstraint (combination of 2 cols (name & phone number) should be unique)

- Write 4 api's to CRUD on a table.
    - create - send the dto back on creation.
    - read - get all records where isDeleted = False
        - read/user_id - to send back only 1 single record.
    - update - only the city column can be updated.
        - on updation, updated_time value should change.
    - delete - update isDelete flag to true (understand hard-delete vs soft-delete)
    - host all 4 url's on swagger.
    - dto, service, serviceImpl usages will be covered.

- flyway integration
    - how to add new tables?
        - add a new table user_country - user_id (FK to user), country
    - how to alter existing table? - rename the column city to currentCity, and add a new column - nativeCity
        = only the currentCity can be updated in the PUT api written before.

- Change the returntype of a user object in /user_id to jsonNode.
- use ObjectMapper to do this.

- Write a custom annotation on GET call (/user_id) to check if the user city is "BLR" then print logs on terminal saying - "User needs to be warned of flooding"

- write custom exception handler to send this exception if user_id is not found. "User might be deleted or does not exist in db"

- Integrate external service - kafka
    - each time a user info is updated, send a record to kafka of this data type format where the values from currentCity will be used.
        - {"userid": 1, "pastCityWas": "", newCityIs: ""}

- Work on task schedulers - db_scheduler library
    - make a simple task to print "Hi! I've started running", for 5 seconds, by putting sleep.
    - design a reporting table - with task name, start time, end time, status, id
    - create an enum file with statuses - STARTED, RUNNING, DONE
    - for each run, an entry should be created in the reportingTable.

- Make a mock table and insert 50000 records in that, with simple 2-3 columns.
    - download some mock excel/csv file from internet with num of records > 40-50K.
    - write an automated script to insert all the records in batches of 500. can be any kind of script.
    - write a sql query "select * from table", and read it in batches of 1000. for each batch of records - print batchId.
        - if there are 50K records, then 50K/1K = 50 batch Id's will be printed on screen.

- add logging to the codebase.
    - for each day a single file should be generated.
    - for each log line - name of class, and function name should be printed.
```

