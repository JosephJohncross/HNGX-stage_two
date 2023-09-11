

# REST API CRUD <br><br>

## About

This repo houses the source code for demonstarting basic understanding of the REST API methodology and how to perform basic crude operations. Below is the detail instruction for the task

You are to build a simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. Your API should dynamically handle parameters, such as adding or retrieving a person by name. Accompany the development with UML diagrams to represent your system's design and database structure. Create an automated testing script that verifies each of your API's operations. Host your entire project on GitHub, and provide a well-structured documentation in the repository that outlines request/response formats, setup instructions, and sample API usage.

## Built with

-   Django and DRF <br><br>

## 🏁 Getting Started <br>


### 📚 Prerequisite

List all things your project needs to work for eg:

-   Python 3
-   Postgres (13 or above)

### Installation

Step by step methods to guide the reader how to setup local dev environment for eg:

1. Clone this repo
1. Setup and start your virtual environment
   - **Window**
   - [Setup virtual environment on windows](https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59) <br>
   - **Linux**
   - [Setup virtual environment on windows](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv.html) <br>
    
1. Install project dependencies

    ```bash
    pip install -r requirements.txt
    ```
1. Setup database<br>
      In your .env file, add the values for your local database
    ```bash
       DB_NAME
       DB_USER
       DB_PASSWORD
       DB_HOST
    ```
1. Run migrations and update database
   ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
1. Start local development server
   ```bash
    python manage.py runserver
    ```
1. Navigate to http://localhost:8000/api<br><br>
_**Viola !!**_ :smile: <br><br>

## Live Demo

https://hngx-stage-two-8l8p.onrender.com/api <br><br>
## Resources

Some articles you can refer to, while building this project

<!-- Add links to all the resources you followed or referred to -->

-   [A How-to Guide on Creating a REST API Using Django REST Framework](https://radixweb.com/blog/create-rest-api-using-django-rest-framework)
-   [Build CRUD API with Django REST framework](https://codevoweb.com/build-crud-api-with-django-rest-framework)
-   [Django REST Framework Views - APIViews](https://testdriven.io/blog/drf-views-part-1/) <br><br>

## 👋 End Note <br>

Did I missed something..? or you have any idea what could be added that will make it better, feel free to contribute I will definitely add that.

The source code of each files, are well documented using the standard python docstring approach.
