# Django

## Part A (Python) - Day 1
```
1. Local Installation
Refer [Python & Pycharm Setup in Windows](https://gist.github.com/raunak-r/15fb871765e56ebe7a05bb6f42fc24d2)
```

## Part B (Data) - Day 2
A small project has to be created in Django now. There will be 2 components (Data & APIs to serve that data), one for each day, and 2 days for spillovers.

Follow these 2 articles completely.
1. [Django project creation](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
2. [SQL Table Design](https://docs.djangoproject.com/en/3.2/intro/tutorial02/)
At the end of this, you should have the same screenshots as shown in the blog running on your localhost in chrome - 

```
Enhancement Task - Make 2 more tables in the same models.py
An Employee table with at least 5 fields
A project table with at least 2 fields.
Constraints - A project cannot be created without 0 employees associated with it.
An employee will work on only one project
```
Refer [Link](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/) for this task.


## Part C (API) - Day 3

Now you've 3 tables in your models.py.
Follow this article, follow the page completely, make new tables if you want, or change the table names as per your project table names. leave the 'post' functions. Work on 'GET' API.
- Refer [Link](https://docs.djangoproject.com/en/3.2/intro/tutorial03/)

At the end of the day - you should have at-least 3 GET API's, one each for each table.
From postman, on calling that API, all the data from that table should be returned.


## Day 4 & 5

1. Import the whole django project to GIT, and send link. Make the project clean and presentable. 
2. Setup and get familiar with Jupyter Notebook Usage 
    - Refer [link](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
    - Task - Import all the singleton python code written for questions to a notebook and make it clean and presentable.
3. Create a new notebook and practice pandas.
    - Task 1 - [Basic Pandas](https://www.datacamp.com/community/tutorials/pandas)
    - Task 2 - [Exploratory Data Analysis using Pandas](https://towardsdatascience.com/exploratory-data-analysis-eda-python-87178e35b14)
    

# Baby Basics
```
https://roadmap.sh/backend
Backend ; https://www.youtube.com/watch?v=0Kv_k4ypj6o
MVC ; https://www.youtube.com/watch?v=DUg2SWWK18I
```

# Basics
```

Django Tutorial by Mosh @YouTube 
https://www.youtube.com/watch?v=rHux0gMZ3Eg&t=890s

Django Tutorial by Telusko @ YouTube 
https://www.youtube.com/watch?v=SIyxjRJ8VNY&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau

Writing first django app @https://docs.djangoproject.com/en/3.2/intro/tutorial01/

Serialization @https://www.django-rest-framework.org/tutorial/1-serialization/

Django Admin - https://www.youtube.com/playlist?list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO
```

# Intermediate
```

Official django guide trumps everything - https://docs.djangoproject.com/en/3.2/intro/tutorial01/
DJANGO ORM - https://books.agiliq.com/projects/django-orm-cookbook/en/latest/
Rest framework - https://www.django-rest-framework.org/tutorial/quickstart/

settings.py usage
how to change db connection.
urls.py usage
how to change admin url to something else
turn debug=off
why debug is needed


Models
Makemigrations, migrate commands
classbased views
functionbasedviews
mapping url & views to send data in postman
using postman to check GET calls.
serializer basic & deserializer

Defining tables in admin.py 
how to see filters in a table in admin page ( list_display & list_filter options)

django ORM 
how to filter, queryset.all(), filter(), 
how to write != in filter queries
2. How to do OR queries in Django ORM? 
3. How to do AND queries in Django ORM? 
4. How to do a NOT query in Django queryset? 
14. How to use Q objects for complex queries?
1. How to model one to one relationships? 
2. How to model one to many relationships? 
3. How to model many to many relationships?
6. How to add a model for a database view? 
7. How to create a generic model which can be related to any kind of entity? (Eg. a Category or a Comment?) 
8. How to specify the table name for a model? 
9. How to specify the column name for model field?
11. How to find second largest record using Django ORM ?
14. How to use Q objects for complex queries? — Django ORM Cookbook 2.0 documentation



Django Management commands - what why
how to run them
write a simple one to just print("hey") as a management command
Custom model_to_dict as a serializer
Reverting django migrations? how to fix messed up migration
where are migrations saved and tracked?
```

# Advanced
```
- select_related & prefetch_related
- triggers
- celery tasks
- api caching
```
