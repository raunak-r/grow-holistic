# ETL
We need you to implement an ETL (Extract, Transform, Load) pipeline using Bonobo, a lightweight ETL framework for Python. The goal is to extract data from a CSV file, transform it, and load it into a PostgreSQL database.

## Please implement the following:
```
Extract: Read data from a CSV file named input_data.csv. Assume this file contains columns id, name, age, and email.
Transform: Perform the following transformations:
Filter out rows where the age is less than 18.
Convert the name column to uppercase.
Ensure the email column is in lowercase.
Load: Insert the transformed data into a PostgreSQL database. Assume the database and table (users) are already set up with columns corresponding to the CSV file.
Please provide the complete code for the Bonobo ETL pipeline, including the necessary setup and connection configurations.
```

## Follow-up Questions:
```
How would you handle large CSV files that might not fit into memory?
What strategies would you use to ensure the ETL process is idempotent and can be safely re-run?
How would you implement error handling and logging within the Bonobo pipeline?
What considerations would you make for scheduling and monitoring this ETL process in a production environment?
```
