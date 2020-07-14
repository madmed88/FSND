# Full Stack API Final Project

# API Reference

# Getting Started

- Base URL: http://127.0.0.1:5000
- Authentication: This API does not rquire authentication

# Error Handling

Erros are returned as JSON objects in the following format:

```
{
  "success": False,
  "error": 400,
  "message": "bad request"
}
```

The API will return three error types when requests fail:

- 400 Bad Request
- 404 Resource Not Found
- 422 Not Processable

# Endpoints

## Get all available categories

**URL** : `/categories`

**Method** : `GET`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "success": true,
  "categories": {
    "1": "category1",
    "2": "category2",
    "3": "category3",
    "4": "category4"
  }
}
```

## Get paginated questions (in groups of 10)

**URL** : `/questions`

**Method** : `GET`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "success": true,
  "questions": [
    {
      "question": "question1",
      "answer": "answer1",
      "difficulty": 1,
      "category": "category1"
    }
    ...
  ],
  "categories": {
    "1": "category1",
    "2": "category2",
    "3": "category3",
    "4": "category4",
  },
  "total_questions": 20
}
```

## Delete question

**URL** : `/questions/:question_id`

**Method** : `DELETE`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "success": true,
    "deleted": 2,
    "questions": [
      {
        "question": "question1",
        "answer": "answer1",
        "difficulty": 1,
        "category": "category1"
      }
      ...
    ],
    "total_questions": 19
}
```

## Add question

**URL** : `/questions`

**Method** : `POST`

**Data example** All fields must be sent.

```json
{
  "question": "q1",
  "answer": "q1",
  "category": 5,
  "difficulty": 4
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "success": true,
    "created": 2,
    "questions": [
      {
        "question": "question1",
        "answer": "answer1",
        "difficulty": 1,
        "category": "category1"
      }
      ...
    ],
    "total_questions": 21
}
```

## Search for question

**URL** : `/questions`

**Method** : `POST`

**Data example** All fields must be sent.

```json
{
  "searchTerm": "title"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "success": true,
    "questions": [
      {
        "question": "title1",
        "answer": "answer1",
        "difficulty": 1,
        "category": "category1"
      }
      ...
    ],
    "total_questions": 21
}
```

## Get questions by category

**URL** : `/category/:category_id/questions`

**Method** : `GET`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "success": true,
  "questions": [
    {
      "question": "question1",
      "answer": "answer1",
      "difficulty": 1,
      "category": "category1"
    }
    ...
  ],
  "currentCategory": "category1",
  },
  "total_questions": 20
}
```

## Get next quizz question

**URL** : `/quizzes`

**Method** : `POST`

**Data example** All fields must be sent.

```json
{
  "previous_questions": [
      {
        "question": "title1",
        "answer": "answer1",
        "difficulty": 1,
        "category": "category1"
      }
      ...
    ],
  "quiz_category": {
    "id": 1,
    "type": "category1"
  }
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "success": true,
  "question": {
    "question": "title2",
    "answer": "answer2",
    "difficulty": 1,
    "category": "category1"
  }
}
```

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup.

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency.

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API.

[View the README.md within ./frontend for more details.](./frontend/README.md)
