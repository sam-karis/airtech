[![CircleCI](https://circleci.com/gh/sam-karis/airtech/tree/develop.svg?style=svg)](https://circleci.com/gh/sam-karis/airtech/tree/develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/61b6e9292ffe0b651fff/maintainability)](https://codeclimate.com/github/sam-karis/airtech/maintainability)
<a href="https://codeclimate.com/github/sam-karis/airtech/test_coverage"><img src="https://api.codeclimate.com/v1/badges/61b6e9292ffe0b651fff/test_coverage" /></a>

## Airtech Flight Booking API

Flight Booking System

# Description

Company Airtech has had their challenges using spreadsheets to manage their flight booking system. They are ready to automate their processes with an application and have reached out to you to build a flight booking application for the company.

## Key Application features

> - Register travellers and admin
> - Log in users
> - Edit profile and upload passport photographs
> - Delete passport photographs
> - Create Flight by admin
> - View all flights
> - Book tickets
> - receive tickets as an email
> - View users tickets
> - View count of tickets in a flight on a specific day

## Development set up

- Check that python 3 is installed:

  ```
  python --v
  >> Python 3.7.4
  ```

- Install virtualenv:

  ```
  pip install virtualenv
  ```

- Check pipenv is installed:

  ```
  virtualenv --version
  >> 16.6.0
  ```

- Check that postgres is installed:

  ```
  postgres --version
  >> postgres (PostgreSQL) 11.4

  ```

- Clone the airtech repo and `cd`` into it:

  ```
  git clone https://github.com/sam-karis/airtech

  ```

- Create and activate the virtualenv:

  ```
  virtualenv virtualenv && source virtualenv/bin/activate
  ```

- Install dependencies:

  ```
  pip install -r requirements.txt
  ```

- Rename the .env_example file to .env and update the variables accordingly:

  ```
    export SECRET_KEY=<secret_key>
    export DATABASE_URL=postgresql://postgres@<host>:<port>/<db_name>
    export CLOUD_NAME=<your_cloud_name_on_cloudinary>
    export API_KEY=<api_key_from_cloudinary>
    export API_SECRET=<secret_key_from_cloudinary>
    export EMAIL_HOST='smtp.gmail.com'
    export EMAIL_USE_TLS=True
    export EMAIL_PORT=587
    export EMAIL_HOST_USER=<your_email_account>
    export EMAIL_HOST_PASSWORD=<email_password>
    export DEFAULT_FROM_EMAIL=<your_email_account>
  ```

- Create database

  ```
  createdb <db_name> # if you have psql installed
  ```

- Apply Migrations:

  ```
  python manage.py migrate
  ```

- Create admin
  ```
  python manage.py createsuperuser
  ```

* Run the application:

  ```
  python manage.py runserver
  ```

* Should you make changes to the database models, run migrations as follows

  ```
  python manage.py makemigration # when you create models or changes are made to existing model
  python manage.py migrate  # applying changes to the database
  ```

* Run tests

  ```
  tox # run all the tests and flake8
  flake8 # check if clean conventions have been followed
  pytest # run tests
  pytest --cov  # test coverage
  ```

* Deactivate the virtual environment once you're done:
  ```
  deactivate
  ```

## Running the API

Manually Test the endpoints with postman

[![Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/4000258/SVfKyqwU?version=latest)

| **EndPoint**                                  | **Functionality**          |
| --------------------------------------------- | -------------------------- |
| POST `/api/v1/auth/register/`                 | Sign up user account       |
| POST `/api/v1/auth/login/`                    | login user                 |
| GET `/api/v1/auth/users/profiles`             | Gets users profiles        |
| GET `/api/v1/auth/users/profiles<username>`   | Gets a user profile        |
| PUT `/api/v1/auth/users/profiles<username>`   | Update profile and image   |
| POST `/api/v1/users/upload`                   | upload image               |
| DELETE `/api/v1/auth/users/profiles/image/`   | delete image               |
| GET `/api/v1/flights`                         | Gets all flights           |
| GET `/api/v1/flights/{{flight-id}}`           | Gets a single flight       |
| POST `/api/v1/flights/{{flight-id}}/tickets`  | Book a ticket on a flight  |
| GET `/api/v1/flights/{{flight-id}}/tickets`   | Get all tickets for a user |
| GET `/api/v1/flights/fn-aeiph89oy/?date=date` | Get tickets on a date      |
| GET `/api/v1/flights/fn-aeiph89oy/`           | Get all tickets for flight |
| GET `/admin`                                  | Admin Dashboard            |

## Testing

locust - `127.0.0.1:8089`

```bash
$ make locust
```

monitoring: endpoint `http://127.0.0.1:8089/`

```bash
$ locust --host=http://127.0.0.1:8000
```
