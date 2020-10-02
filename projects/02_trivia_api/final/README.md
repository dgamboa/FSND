# Full Stack Trivia Application

This is the second major project in the Udacity Full Stack nanodegree. The source code from Udacity comes with a pre-built React frontend that needs minor updates. The backend is mostly empty for students to build a fully functioning API to be tested with unittest, curl and ultimately to be linked to the pre-built frontend. The primary objective of the project is to practice structuring API endpoints by implementing Flask, CORS, routes, HTTP, curl, TDD and JSON, among other supporting technologies and modules.

The Trivia Application consists of a database of trivia question and answers classified into various categories. Users have the ability to display questions, show answers, add questions, delete questions, search for questions as well as play a quiz game that randomizes questions and tracks score.

## Getting Started: Backend

### Pre-Requisites and Local Development
In order to use this project, users will need to install Python3, pip and node on their local environments. To get started, navigate to the backend directory and follow these instructions:

### Dependencies
To ensure all dependencies are installed run:
```
pip install -r requirements.txt
```

### Database
In order to populate the database with a starter set of questions, run:
```
psql trivia < trivia.psql
```

### Running App
To run the application, execute the following from the command line:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

The backend application will now be running on `http://127.0.0.1:5000/` and can be accessed via curl.

### Testing
To execute the endpoint test suite included in the API, run:

> Make sure to exclude `dropdb` when running for the first time since the database doesn't yet exist in the local environment

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python3 test_flaskr.py
```

## Getting Started: Frontend

### Dependencies
The frontend uses [Node.js](https://nodejs.org/en/) and [Node Package Manager](https://www.npmjs.com/). It is built using [React](https://reactjs.org/), which is a JavaScript library for developing user interfaces. To install npm, simply navigate to the frontend directory and run:
```
npm install
```

### Running Frontend
To run the frontend application that links to the backend, execute the following from the command line:
```
npm start
```

## API Reference


## Authors
* Daniel Gamboa, Udacity Full Stack Nanodegree Student
* Udacity Project Development Team

## Acknowledgements
Thank you to the Udacity team for developing a fun and difficult exercise so I could learn by doing. Also, a big shout out to the Knowledge Database and the Mentors who diligently answer students' questions.
