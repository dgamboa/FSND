# Coffee Shop Full Stack Application

This is the third major project in the Udacity Full Stack nanodegree. The source code from Udacity comes with a pre-built React frontend that requires configuring the environment variables to connect to the appropriate Auth0 service. The backend includes a pre-built drinks model to facilitate the development of menu API. The primary objective of the project is to implement authentication and permissions functionality using Auth0 and develop the endpoints to be able to GET, POST, PATCH and DELETE drinks in a coffee shop menu. In addition to being able to perform these functions through the browser using the frontend interface, users should also be able to use properly structured Postman requests with the appropriate tokens to interact with the database.

The Coffee Shop Application consists of a menu populated from a drinks database that includes the drink's name and recipe. There are three types of users:

1) Public: can view drink names and graphics.
2) Baristas: can view drink names, graphics and recipes.
3) Managers: can create, view, edit and delete drinks and recipes.

## Getting Started

### Backend Pre-Requisites and Local Development
In order to get started, you will need [Python3](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) and [pip](https://pypi.org/project/pip/) on your local environment. In order to keep dependencies separate and organized, you should consider setting up a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) as well.

#### Dependencies

Navigate to the backend directory and follow these instructions:

```
pip install -r requirements.txt
```

This will install all of the required packages within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

#### Running the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```
export FLASK_APP=api.py;
```

To run the server, execute:

```
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

[For more on the backend, please refer to the README.md within the ./backend directory.](./backend/README.md)

### Frontend Pre-Requisites and Local Development

In order to connect the frontend to the Flask-based backend, you will need Nodejs and Node Package Manager (NPM). These can be jointly downloaded from https://nodejs.org/en/download/.

You will also need the Ionic Command Line Interface to serve and build the frontend. Instructions for installing it can be found [here](https://ionicframework.com/docs/installation/cli).

#### Dependencies

To install all project dependencies in the package.json file located in the `./frontend` directory, open your terminal and run:

```
npm install
```

After that ensure that the proper environment variables are set inside `./src/environments/environments.ts`

#### Running the Frontend Server

To activate the Ionic development server, cd into the `frontend` directory and run:

```
ionic serve
```

##



## About the Stack

The Coffe Shop Application backend is based on the Flask framework in Python. It uses SQLAlchemy to interface with a SQLite database with a single Drinks table. Authentication and permissions are managed with Auth0.

The frontend is built in React and uses Ionic to interface with data from the Flask server.
