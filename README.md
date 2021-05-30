# Basic TVM

Created this simply as a way to to experiment with using the Django REST Framework to create an AWS Token Vending Machine.

## Requirements

- Poetry
- sqlite3 libraries
- A set of IAM credentials in one of the standard locations Boto3 can find.
- An IAM Role named `tvmtest` configured in each account you wish to return credentials for, e.g. `arn:aws:iam::{account}:role/tvmtest`

## Installation

1. `poetry shell`

1. `poetry install`

1. `./src/manage.py migrate`

1. `./src/manage.py createsuperuser`

    In this setup doc we'll just use `admin/welcome`.

1. `./src/manage.py runserver`

1. Login to http://localhost:8000/admin and add a Command entry which consists of a Command name which will be called via the API and the AWS IAM Identity policy document. Make sure you also check the `Enable` box.

1. Call the API using curl

    ```text
    curl -H 'Accept: application/json; indent=4' -u admin:welcome http://127.0.0.1:8000/api/v1/credentials/<command>/<account>/
    ```

    Command being the Command model entry you created, account being an AWS account number to assume the standard IAM Role in and return credentals for.

