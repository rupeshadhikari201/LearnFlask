# Flask Project: Building a RESTful API with SQLite Database

## Overview

This project demonstrates how to build a RESTful API using Flask, a micro web framework for Python. The API utilizes a SQLite database, which is a file-based database and does not require setting up a separate server. The project also employs SQLAlchemy for Object-Relational Mapping (ORM), Marshmallow for object serialization and deserialization, and several other Flask extensions for authentication, email, and more.

## Features Implemented

### 1. Setting Up the Flask Project and Server

- The project starts with setting up a basic Flask application, including creating the necessary files and directories, and configuring the development server.

### 2. Working with JSON, HTTP Status Codes, URL Parameters, and URL Variables

- The API handles JSON data, uses appropriate HTTP status codes for responses, and utilizes URL parameters and variables to manage different routes and endpoints.

### 3. Setting Up SQLAlchemy and Creating ORM Model Classes

- SQLAlchemy is used to interact with the SQLite database. This includes creating ORM model classes to define the structure of the data stored in the database and seeding the database with initial data.

### 4. Serializing SQLAlchemy Results with Marshmallow

- Marshmallow is used to serialize and deserialize data between the SQLAlchemy models and JSON responses. This ensures that the data is properly formatted for API consumers.

### 5. JSON Web Tokens, User Authentication, and Email Password Recovery

- The project implements user authentication using JSON Web Tokens (JWT) with the `Flask-JWT-Extended` library. It also includes features for email password recovery using `Flask-Mail`.

### 6. CRUD Operations

- The API supports basic CRUD (Create, Read, Update, Delete) operations for managing data in the database. This includes endpoints for adding, retrieving, updating, and deleting resources.

## Libraries Used

- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, allowing you to use a powerful ORM in your Flask application.

  - [Documentation](https://flask-sqlalchemy.readthedocs.io/en/3.1.x/)

- **Flask-Login**: Provides user session management for Flask.

  - [Documentation](https://flask-login.readthedocs.io/en/latest/)

- **Flask-User**: Provides a basic user authentication system for Flask.

  - [Documentation](https://flask-user.readthedocs.io/en/latest/)

- **Flask-JWT-Extended**: Implements JSON Web Tokens for authentication.

  - [Documentation](https://flask-jwt-extended.readthedocs.io/en/stable/)

- **Flask-Marshmallow**: Provides integration between Flask and Marshmallow for serialization and deserialization.

  - [Documentation](https://flask-marshmallow.readthedocs.io/en/latest/)

- **Flask-Mail**: Handles email sending within the Flask application.
  - [Documentation](https://flask-mail.readthedocs.io/en/latest/)

## APIs in This Project

### Endpoints

- **Root Endpoint**

  - `http://localhost:5000/`
  - Displays a welcome message or basic information about the API.

- **User Registration**

  - `http://localhost:5000/register`
  - Allows users to register with the application.

- **User Login**

  - `http://localhost:5000/login`
  - Generates an access token for authenticated users.

- **Password Recovery**

  - `http://localhost:5000/retrieve_password/your_email` (replace `your_email` with the user's email)
  - Sends a password recovery email to the specified user.

- **Planet Details**

  - `http://localhost:5000/planet_details/planet_id` (replace `planet_id` with the ID of the planet)
  - Retrieves details of a specific planet.

- **Add Planet**

  - `http://localhost:5000/add_planet`
  - Creates a new planet entry in the database.

- **Update Planet**

  - `http://localhost:5000/update_planet`
  - Updates an existing planet entry in the database.

- **Delete Planet**
  - `http://localhost:5000/delete_planet/planet_id` (replace `planet_id` with the ID of the planet)
  - Deletes a planet entry from the database.

## Environment Variables

- The project uses `.env` or `.flaskenv` files to manage environment variables. To use these files, you need to install `python-dotenv`:
  ```bash
  pip install python-dotenv
  ```

# Getting Started

## 1. Clone the Repository

    ```
    git clone https://github.com/your-repo-url.git
    ```

## 2. Navigate to the Project Directory

    ```
    cd your-project-directory
    ```

## 3. Create and Activate a Virtual Environment

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate  # On Windows
    ```

## 4. Install Dependencies

    ```
    pip install -r requirements.txt
    ```

## 5. Setup Your .env File

    ```
    pip install python-dotenv
    ```
    Setup your `.env file with your gmail's App password to send email.

## 6. Run the Application

    ```
    flask run --host=0.0.0.0
    ```

# Notes

    * Ensure you have Python and Flask installed on your system.
    * The development server is suitable for testing but should not be used in production. For  production deployment, consider using a WSGI server like Gunicorn and a reverse proxy server like Nginx or Apache.
