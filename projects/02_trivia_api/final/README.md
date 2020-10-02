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

### Getting Started
* This app can only be run locally. The backend app is hosted at `http://127.0.0.1:5000/` and the frontend app is hosted at `http://127.0.0.1:3000/`. There is no requirement for authentication.

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
* 405: Method Not Allowed
* 422: Not Processable
* 500: Internal Server Error

### Endpoints
#### GET /categories
* Returns a list of category objects and the total number of categories
* Sample: `curl http://127.0.0.1:5000/categories`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
}
```

#### GET /questions
* Returns a list of question objects, a list of category objects and the total number of questions. The list of questions is paginated in groups of 10 questions.
* Sample: `curl http://127.0.0.1:5000/questions`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```

#### DELETE /questions/{question_id}
* Deletes the questions with the specified id and returns the deleted question's id, a list of paginated question objects, a list of category objects and the total number of questions.
* Sample: `curl -X DELETE http://127.0.0.1:5000/questions/2`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "deleted": 2,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

#### POST /questions
* This endpoint can be used to create new questions or to search for existing questions:
  * Create Questions: uses the submitted question, answer, category and difficulty to create a new question. Returns the id of the created question, a list of paginated question objects, the total number of questions and a list of category objects.
  * Search for Questions: uses the terms submitted to search for a question. Returns a list of paginated question objects matching the submitted terms as well as the total number of questions matching.
* Sample Create: `curl -X POST http://127.0.0.1:5000/questions 'Content-Type: application/json' -d '{"question": "What is the capital of the United States?", "answer": "Washington DC", "category": "2", "difficulty": "1"}'`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "created": 26,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```
* Sample Search: `curl -X POST http://127.0.0.1:5000/questions -H 'Content-Type: application/json' -d '{"searchTerm": "capital"}'`
```
{
  "current_category": null,
  "questions": [
    {
      "answer": "Washington DC",
      "category": 2,
      "difficulty": 1,
      "id": 24,
      "question": "What is the capital of the United States?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

#### GET /categories/{int:category_id}/questions
* Returns the chosen category, a list of question objects based on that category and the total number of questions in that category.
* Sample: `curl http://127.0.0.1:5000/categories/6/questions`
```
{
  "current_category": "Sports",
  "questions": [
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```

#### POST /quizzes
* This endpoint enables the quiz trivia game. It can be played for all categories or for a specific category by selecting a category type. For example, the below sample specifies Science as the category in which to play. The endpoint returns a random question object and it tracks the previous questions in order to avoid repetition.
* Sample: `curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20,22], "quiz_category": {"type": "Science", "id": "1"}}' localhost:5000/quizzes`
```
{
  "current_question": {
    "answer": "Alexander Fleming",
    "category": 1,
    "difficulty": 3,
    "id": 21,
    "question": "Who discovered penicillin?"
  },
  "previous_questions": [
    20,
    22
  ],
  "success": true
}
```

## Authors
* Daniel Gamboa, Udacity Full Stack Nanodegree Student
* Udacity Project Development Team

## Acknowledgements
Thank you to the Udacity team for developing a fun and difficult exercise so I could learn by doing. Also, a big shout out to the Knowledge Database and the Mentors who diligently answer students' questions.
