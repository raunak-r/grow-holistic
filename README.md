# Flight Booking System

## Overview

This is a flight booking system that allows users to search for flights, book flights, and manage their bookings. The system is implemented using a RESTful API.

## APIs

The following APIs are implemented:

* **GET /bookings/<user_id>**
    * Get all the bookings for a user.
* **GET /flights/<airline_id>**
    * Get all the flights for an airline.
* **GET /flights/<arr_city>/<dep_city>**
    * Get all the flights between two cities.
* **GET /flight/results/**
    * Search for flights between two cities on a specific date.
    * Used HTML form with From, to and date to send the data and also used POST method, so that sending data won't show-up in the Url

## Usage

To use the system, you will need to make HTTP requests to the APIs. The following examples show how to make requests to the APIs:

* **Get all the bookings for a user:**


curl -X GET http://localhost:8080/bookings/<user_id>
```

* **Get all the flights for an airline:**

```
curl -X GET http://localhost:8080/flights/<airline_id>
```

* **Get all the flights between two cities:**

```
curl -X GET http://localhost:8080/flights/<arr_city>/<dep_city>
```

* **Search for flights between two cities on a specific date:**

```
curl -X GET http://localhost:8080/flight/results/		

use the form in the Home Page to send the Search Details or Use the POST method with <arr_city>, <dep_city>, <date:yyyy-mm-dd> and also CSRF token (please don't me how to do ! :) 

## Development

The system is developed using the following technologies:

* Python
* Django
* PostgreSQL

