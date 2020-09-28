# API Project Notes
## General lessons learned from the Udacity Trivia API build out

### Set Up Application
1. Confirm Python 3.7 is installed with `python -V`
2. Set up the virtual environment using the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. With the virtual environment set up and running, navigate to the `backend/` directory install dependencies included in the requirements.txt file with `pip install -r requirements.txt`
4. Create the database by running `dropdb trivia && createdb trivia`
5. Set up the database using the psql file provided by running `psql trivia < trivia.psql`
6. Run the server from the `backend/` directory:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

### Set Up Testing
1. Create the test database by running `dropdb trivia_test && createdb trivia_test`
2. Set up the database using the psql file provided by running `psql trivia_test < trivia.psql`
3. Run the test file by running `python3 test_file_name.py` to make sure everything is working
> Note: at this point it should return something like "Ran 0 tests in 0.000s OK"

### Developing the Application with TDD
1. Write the first test, in this case to handle GET requests for all available categories, and make sure it fails; then write the endpoint that will make it pass
