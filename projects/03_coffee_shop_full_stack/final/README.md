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

## API Reference

This app can only be run locally. The backend app is hosted at `http://127.0.0.1:5000/` and the frontend app is hosted at `http://127.0.0.1:8100/`. Authentication is performed through a third-party service called [Auth0](https://auth0.com/).

### Error Handling
If a request fails, the error object will include the following parameters in JSON format:
```
{
  'success': False,
  'error': 404,
  'message': 'resource not found'
}
```
Other errors handled by the API include:
* 400: Bad Request
* 401: Unauthorized
* 422: Not Processable
* 500: Internal Server Error

### Endpoints
These may accessed via [curl](https://curl.haxx.se/), [Postman](https://www.postman.com/) or the frontend interface.

#### GET /drinks
* Returns a list of drinks along with their ids, names and the short version of the recipes, which includes only the ingredient color and how many parts are needed to make the drink
* Open to all users
```
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "#e1f2ec",
                    "parts": 1
                }
            ],
            "title": "Milk"
        },
        {
            "id": 2,
            "recipe": [
                {
                    "color": "#e1f2ec",
                    "parts": 2
                },
                {
                    "color": "black",
                    "parts": 1
                }
            ],
            "title": "Latte"
        },
        {
            "id": 3,
            "recipe": [
                {
                    "color": "#f4f9fc",
                    "parts": 1
                },
                {
                    "color": "#e1f2ec",
                    "parts": 1
                },
                {
                    "color": "black",
                    "parts": 1
                }
            ],
            "title": "Capuccino"
        },
        {
            "id": 4,
            "recipe": [
                {
                    "color": "#84cef9",
                    "parts": 1
                }
            ],
            "title": "Water"
        }
    ],
    "success": true
}
```

#### GET /drinks-detail
* Returns a list of drinks along with their ids, names and the long version of the recipes, which includes the ingredient color, the ingredient name and how many parts are needed to make the drink
* Requires manager- or barista-level permissions
```
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "#e1f2ec",
                    "name": "Milk",
                    "parts": 1
                }
            ],
            "title": "Milk"
        },
        {
            "id": 2,
            "recipe": [
                {
                    "color": "#e1f2ec",
                    "name": "Milk",
                    "parts": 2
                },
                {
                    "color": "black",
                    "name": "Coffee",
                    "parts": 1
                }
            ],
            "title": "Latte"
        },
        {
            "id": 3,
            "recipe": [
                {
                    "color": "#f4f9fc",
                    "name": "Froth",
                    "parts": 1
                },
                {
                    "color": "#e1f2ec",
                    "name": "Milk",
                    "parts": 1
                },
                {
                    "color": "black",
                    "name": "Espresso",
                    "parts": 1
                }
            ],
            "title": "Capuccino"
        },
        {
            "id": 4,
            "recipe": [
                {
                    "color": "#84cef9",
                    "name": "Water",
                    "parts": 1
                }
            ],
            "title": "Water"
        }
    ],
    "success": true
}
```

#### POST /drinks
* Creates a new drink including its name and recipe
* Requires manager-level permissions
```
{
    "drinks": {
        "id": 5,
        "recipe": [
            {
                "color": "blue",
                "name": "Water",
                "parts": 1
            }
        ],
        "title": "Water3"
    },
    "success": true
}
```

#### PATCH /drinks/{drink_id}
* Updates a drink's name, recipe or both
* Requires manager-level permissions
* Sample body of request:
```
{
    "title": "OJ",
    "recipe": [{
        "name": "Oranges",
        "color": "orange",
        "parts": 1
    }]
}
```
* Sample body of response:
```
{
    "drinks": [
        {
            "id": 5,
            "recipe": [
                {
                    "color": "orange",
                    "name": "Oranges",
                    "parts": 1
                }
            ],
            "title": "OJ"
        }
    ],
    "success": true
}
```

#### DELETE /drinks/{drink_id}
* Deletes a drink record from the menu
* Requires manager-level permission
```
{
    "delete": "5",
    "success": true
}
```

## About the Stack

The Coffee Shop Application backend is based on the [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework in Python. It uses [SQLAlchemy](https://www.sqlalchemy.org/) to interface with a [SQLite](https://sqlite.org/index.html) database with a single Drinks table. Authentication and permissions are managed with [Auth0](https://auth0.com/).

The frontend is built in [React](https://reactjs.org/) and uses [Ionic](https://ionicframework.com/docs/v3/api/IonicModule/) to interface with data from the Flask server.

## Key Lessons Learned
* Avoid bare exceptions. For a refresher [read this](https://realpython.com/the-most-diabolical-python-antipattern/).
* Ensure tokens have sufficient expiration runways by adjusting the time (in seconds) in the Auth0 application settings.
* 

## Authors
* Daniel Gamboa, Udacity Full Stack Nanodegree Student
* Udacity Project Development Team

## Acknowledgements
Thank you to the Udacity team for developing another fun and difficult exercise.
