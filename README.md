# Django Quiz Application

This is a Django-based application that allows users to create and participate in timed quizzes. The application provides a RESTful API for creating and retrieving quizzes. Users can create quizzes, get the active quiz, retrieve quiz results, and retrieve all quizzes.

## Features

- Create a Quiz: Users can create a quiz by sending a POST request to the API with the necessary fields such as question, options, rightAnswer, startDate, and endDate.
- Get Active Quiz: Users can retrieve the active quiz, which is the quiz currently within its start and end time.
- Get Quiz Result: After the specified time period of a quiz has ended, users can retrieve the result of the quiz.
- Get All Quizzes: Users can retrieve all the quizzes available in the system.

## Requirements

- Python (version 3.6 or higher)
- Django (version 3.2 or higher)
- Django REST Framework (version 3.12 or higher)

## Project Description: Quiz Management System API

This project is a Quiz Management System API built using Python and Django. The API allows users to create and participate in timed quizzes. It provides various functionalities for managing quizzes, retrieving active quizzes, and getting quiz results.

### Functionalities:
1. Create a Quiz: Users can create a new quiz by sending a POST request to the API. The required fields include the question, options (answer choices), rightAnswer (index of the correct answer), startDate (quiz start date and time), and endDate (quiz end date and time).

2. Get Active Quiz: Users can retrieve the active quiz (the quiz that is currently within its start and end time) by sending a GET request to the "/quizzes/active" endpoint.

3. Get Quiz Result: After the end time of a quiz, users can retrieve the result of the quiz by sending a GET request to the "/quizzes/:id/result" endpoint, where ":id" represents the ID of the quiz. The result includes the question and the right answer.

4. Get All Quizzes: Users can retrieve all quizzes by sending a GET request to the "/quizzes/all" endpoint. This provides a list of all quizzes with their respective question, status, and quiz ID.

### API Endpoints:

* POST /quizzes: Create a new quiz.
* GET /quizzes/active: Retrieve the active quiz.
* GET /quizzes/:id/result: Retrieve the result of a quiz by its ID.
* GET /quizzes/all: Retrieve all quizzes.

### Additional Features:

* Quiz Status: Each quiz has a status field, which is automatically updated based on the start and end time of the quiz. The possible statuses are "inactive" (before the start time), "active" (during the available time), and "finished" (after the end time).

* Error Handling: The API implements error handling for all endpoints and returns appropriate error responses in case of missing fields, invalid input, or unavailable quiz results.

* Rate Limiting: The API implements rate limiting to prevent abuse and control the number of requests from a single user or IP address.

* Caching: The API incorporates caching to improve the response time of frequently accessed data, enhancing the overall performance of the system.

* Scheduled Quiz Status Update: A management command is implemented to update the status of quizzes based on their start and end time. This command can be run periodically using a cron job.

The project code is organized in a well-structured manner, ensuring readability and maintainability. It includes the necessary models, views, and management commands for the quiz management system.

Please refer to the provided code and documentation for a more detailed understanding of the implementation and usage of the Quiz Management System API.
