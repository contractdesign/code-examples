
# Notes on Using a Python Virtual Environment

To set up a Python virtual environment, run the following commands
(see [Miguel Grinberg](https://github.com/miguelgrinberg/REST-auth
""))

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt


To generate the requirements from the packages already installed in an
environment, use pip freeze:

    $ pip freeze > requirements.txt


