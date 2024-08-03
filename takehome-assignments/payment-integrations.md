# Payment Integration
As an applicant, your task is to set up a project that accomplishes a simple checkout-to-payment flow using Flask for the backend, Stripe for the payment gateway, and PostgreSQL as the database.

## Project Requirements:
Create a Flask Project:
```
Set up a Flask project with two tables: Product and Transactions.
The Product table should have 3 offerings with fields such as id, name, description, and price.
The Transactions table should capture id, product_id, status, transaction_id, amount, and any other relevant data.
```

Create an Angular Frontend:
```
Set up a small frontend project in Angular with a single homepage that loads the 3 product offerings from the backend.
Each offering should have a "Buy" button below it.
```

Integrate Payment with Stripe:
```
On clicking the "Buy" button, load a payment page using Stripe's API in sandbox mode.
Capture the payment status, transaction id, and other relevant data in the backend.
```

Handle Payment Status:
```
Ensure the backend captures and stores the payment status, transaction id, and relevant data in the Transactions table.
On successful payment, show a notification to the client with the message "Success".
```

## Deliverable:
Create a repository on your personal GitHub and create two folders, one each for backend and frontend in the same repo with all the codes.
You are expected to have a minimum of 5 commits, demonstrating the growth of the code over the course of your project.

## Follow-up Questions:
```
How would you ensure the security of the payment process?
What strategies would you use to handle errors during the payment process?
How would you test the payment integration to ensure it works correctly?
How would you handle different payment statuses (e.g., success, failure, pending)?
```
