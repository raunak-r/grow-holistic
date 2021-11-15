# Python and Django in 7 Days

## Part A (Python) - Day 1


1. Local Installation
Refer [Python & Pycharm Setup in Windows](https://gist.github.com/raunak-r/15fb871765e56ebe7a05bb6f42fc24d2)

2. Python Basics - A few questions to refresh python memory.
- [Python Question Bank Link](https://www.w3resource.com/python-exercises/) - first question of each topic mentioned below
```
Python Basic (Part -I) [ 150 Exercises with Solution ]
Python Basic (Part -II) [ 142 Exercises with Solution ]
Python built-in Modules [ 31 Exercises with Solution ]
Python Data Types - String [ 101 Exercises with Solution ]
Python JSON [ 9 Exercises with Solution ]
Python Data Types - List [ 272 Exercises with Solution ]
Python Data Types - Dictionary [ 80 Exercises with Solution ]
Python Conditional statements and loops [ 44 Exercises with Solution]
Python functions [ 21 Exercises with Solution ]
Python Lambda [ 52 Exercises with Solution ]
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


## Day 4
#### In case Python is very weak and day 1 is spilled over.
- Spend the first 2 days practicing python and local installation (Part A)

#### If Part B & C has leftovers.
- Take one more day to complete it.

#### If Part B & C is done on time
- Implement POST API for the 3 tables. Refer [Link](https://www.askpython.com/django/django-rest-api)
- Start Day 5.

## Day 5

1. Import the whole django project to GIT, and send link. Make the project clean and presentable. 
2. Setup and get familiar with Jupyter Notebook Usage 
    - Refer [link](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
    - Task - Import all the singleton python code written for questions to a notebook and make it clean and presentable.
3. Create a new notebook and practice pandas.
    - Task 1 - [Basic Pandas](https://www.datacamp.com/community/tutorials/pandas)
    - Task 2 - [Exploratory Data Analysis using Pandas](https://towardsdatascience.com/exploratory-data-analysis-eda-python-87178e35b14)
    
