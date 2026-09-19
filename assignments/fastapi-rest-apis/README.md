# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API with FastAPI by creating endpoints that read, create, and search a collection of books. You will practice HTTP methods, JSON responses, path parameters, request validation, and status codes.

## 📝 Tasks

### 🛠️ Create a GET Endpoint for Books

#### Description

Use the provided starter code to create an endpoint that returns all books in the in-memory catalog. Run the FastAPI application with Uvicorn and test the endpoint in the automatic documentation at `/docs` or with an API client.

#### Requirements

Completed program should:

- Start a FastAPI application from `starter-code.py`
- Implement `GET /books`
- Return the current books as a JSON list
- Include each book's `id`, `title`, and `author`


### 🛠️ Add and Validate New Books

#### Description

Define a Pydantic request model and add an endpoint that accepts a new book. The API should create an ID for the book and return the saved book to the client.

#### Requirements

Completed program should:

- Define a request model requiring a non-empty `title` and `author`
- Implement `POST /books`
- Accept a JSON request body such as `{ "title": "The Hobbit", "author": "J.R.R. Tolkien" }`
- Add the new book to the in-memory catalog with a unique integer ID
- Return the created book with HTTP status code `201`
- Let FastAPI return a validation error for missing or invalid required fields


### 🛠️ Retrieve One Book Safely

#### Description

Create an endpoint for looking up one book by its ID. A valid ID should return the matching book, while an unknown ID should produce a useful HTTP error instead of returning an empty response.

#### Requirements

Completed program should:

- Implement `GET /books/{book_id}`
- Return the matching book when the ID exists
- Raise an HTTP 404 error when the ID does not exist
- Include a clear error detail message in the 404 response


### 🛠️ Stretch: Search the Catalog

#### Description

Extend `GET /books` with an optional `author` query parameter. When the parameter is provided, return only books whose author matches the search text, ignoring letter case.

#### Requirements

Completed program should:

- Support requests such as `GET /books?author=tolkien`
- Return all books when `author` is omitted
- Match authors without treating uppercase and lowercase letters as different
- Keep the response as a JSON list, including an empty list when there are no matches
