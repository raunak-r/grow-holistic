# MYSQL

Refer - https://www.geeksforgeeks.org/30-days-of-sql-from-basic-to-advanced-level/
Before you start, save all these scripts under the folder name 'database-notes' on your personal git account.

### Baby Basics
```
https://www3.ntu.edu.sg/home/ehchua/programming/sql/MySQL_HowTo.html#zz-1

Before proceeding, make a git repo by the name of mysql-demo or postgres-demo
and save all the scripts in its own individual file.

At the end of this exercise you will have around 3-4 scripts saved.
```

The following topics have to be done
```
1.  Introduction to Relational Database and SQL
1.1  Relational Databases
1.2  Structure Query Language (SQL)
1.3  SQL By Examples
2.  Introduction to MySQL Relational Database Management System (RDBMS)
3.  How to Install MySQL 8.0 and Get Started with SQL Programming
3.1  Step 0: Create a directory to keep all your works
3.2  Step 1: Download and Install MySQL
3.3  Step 3: Start the "Server"
3.4  Step 4: Start a "Client"
3.5  Step 5: Change the Password for the Superuser "root"
3.6  Step 6: Create a New User
3.7  Step 7: Create a new Database, a new Table in the Database, Insert Records, Query and Update
3.8  More Exercises
4.  Many-to-many Relationship
```

### Basic
```
Creating Database: This concept will make you learn how to create your own database.
Creating Tables and adding data: From this concept, you will learn how to create tables inside the database and insert data in them.
PRIMARY KEYS, FOREIGN KEYS.
SELECT Clause: Retrieve or fetch data from a database.
FROM Clause: From which table in the database you have to select data.
WHERE Clause: It forms the condition based on which data have to be queried.
DELETE Statement: For deletion tasks.
INSERT INTO: For insertion tasks.
AND and OR operator: Selecting data based on AND or operator.
Drop and Truncate: It will drop or truncate the collection as per the condition.
NOT Operator: It will select the data which is not based on the given condition.
```

### Intermediate
```
WITH Clause: Understanding the concept of with clause and using it to give the sub-query block a name.
FETCH Clause: It will fetch the filtered data based upon certain conditions like fetching only the top 3 rows.
Arithmetic Operators: Using arithmetic operators to filter the data conveniently and precisely.
Wildcard Operators: To intelligently select the exact data like names starting or ending with T.
UPDATE Statement:  Updating certain data entries based upon the condition provided.
ALTER Table: Adding, dropping, or modifying table based on the given condition.
LIKE Clause: It will follow the pattern given on the condition for search.
BETWEEN and IN operator:  It will select the data range between or in the given condition.
CASE Statement: It will check for the conditionals and will query the data as per the respective case.
EXISTS: It will form the nested query to filter out the data which exists in another query.

DISTINCT Clause: It will select only the distinct data, not repetitive.
Count Function: Returns the total count of the data filtered.
Sum Function: Return the sum of all the data being queried.
Average Function: Return the average of all the data being queried.
Minimum Function: It will return the minimum data from the whole data that is being queried.
Maximum Function: It will return the maximum data from the whole data that is being queried.
ORDER BY: This statement will order the queried data as per your convenience like in ascending or descending order.
GROUP BY: This statement will group all your queried data with the column given in the condition.
ALL and ANY Clause: They are logical operators in SQL and return boolean value as a result.
TOP Clause: Used to fetch the limited number of rows from a database.
```

### Advanced
```
Union Clause: Just like the mathematical union operator, this clause will make the union of the tables given.
Intersection Clause: It will join the two or more tables where they are intersecting.
Aliases: It will give an alias to the table which we can refer to as later.
Cartesian Join and Self Join: Sometimes to query out some data, we have to self join the table to itself.
Inner, Left, Right and Full Joins: These four types of join comes into play when we have to join one table with another. Look upon their syntax and learn to deal with these joins.
Division Clause: Division is typically required when you want to find out entities that are interacting with all entities of a set of different types of entities.
Using Clause: If several columns have the same names but the datatypes do not match, the NATURAL JOIN clause can be modified with the USING clause to specify the columns that should be used for an EQUIJOIN.
Combining values: Combining aggregate and non-aggregate values in SQL using Joins and Over clause.
MINUS Operator: It is used as “except” which means it will join the two intersecting tables and will minus one table so that only the intersection and the other table is covered.
Joining 3 or more tables: Although used very rarely but this will make you learn and understand how to join 3 or more tables and then carry out the querying operations.

```

# Task
```
Enhancement Task - Design a 2 table DB.
An Employee table with at least 5 fields
A project table with at least 2 fields.
Constraints - A project cannot be created without 0 employees associated with it.
An employee will work on only one project.
```
