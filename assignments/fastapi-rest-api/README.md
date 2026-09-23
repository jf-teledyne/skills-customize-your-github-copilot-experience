# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a simple REST API using FastAPI to manage a list of tasks or items. This assignment focuses on building routes, handling JSON data, validating inputs, and returning clean API responses.

## 📝 Tasks

### 🛠️ Set Up the API

#### Description
Create a FastAPI app and set up a basic project structure that can respond to HTTP requests and serve JSON data.

#### Requirements
Completed program should:

- install and import FastAPI
- create an app instance using `FastAPI()`
- define a root endpoint that returns a welcome message
- run the app locally with a development server
- verify the API responds correctly in the browser or with a client

### 🛠️ Build CRUD Endpoints

#### Description
Implement the main CRUD routes for a small resource such as tasks, books, or students.

#### Requirements
Completed program should:

- provide a `GET` endpoint to list all items
- provide a `GET` endpoint to fetch one item by its ID
- provide a `POST` endpoint to create a new item
- provide a `PUT` or `PATCH` endpoint to update an existing item
- provide a `DELETE` endpoint to remove an item
- return JSON responses for every request

### 🛠️ Validate Data and Improve the API

#### Description
Use Pydantic models and FastAPI features to validate inputs and make the API easier to use and maintain.

#### Requirements
Completed program should:

- define a request model for creating or updating items
- validate required fields such as title, description, or status
- use response models or structured return data for clarity
- include descriptive status codes such as `200`, `201`, and `404`
- handle common error cases cleanly and predictably

### 🛠️ Add Optional Enhancements

#### Description
Improve the API by adding a few practical features that make it feel complete and production-ready.

#### Requirements
Completed program should:

- support query parameters or filtering
- include a simple search or sorting feature
- document the API using FastAPI's built-in interactive documentation
- keep the code organized with small helper functions or separate model definitions
