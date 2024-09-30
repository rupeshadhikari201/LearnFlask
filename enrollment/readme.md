## Method 01 to turn on Debug mode on:

    ```
    $env:FLASK_DEBUG = "1"     # For PowerShell
    set FLASK_DEBUG=1          # For cmd
    export FLASK_DEBUG=1       # For Linux/macOS
    flask run
    ```

## Method 02 to turn on Debug mode on:

    ```
    $env:FLASK_ENV = "development"      # On Windows,
    set FLASK_ENV=development
    export FLASK_ENV=development        # On Linux/macOS:
    flask run
    ```

## Mongodb comands

    mongod --version
    mongo --version

## Libraries Used

- Flask-MongoEngine https://docs.mongoengine.org/projects/flask-mongoengine/en/latest/index.html pip install git+https://github.com/idoshr/flask-mongoengine.git@1.0.1
- Flask-WTF https://flask-wtf.readthedocs.io/en/1.2.x/ pip install -U Flask-WTF
- Flask-Security https://flask-security-too.readthedocs.io/en/stable/ pip install flask-security
