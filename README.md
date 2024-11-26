
# Python GraphQL Strawberry Examples

This repository demonstrates examples of using the [Strawberry GraphQL](https://strawberry.rocks/) library hosted on [FastAPI](https://fastapi.tiangolo.com/) service

## Project Structure

- `main.py`: Entry point for the application.
- `models.py`: Contains data models for the GraphQL schema.
- `resolvers.py`: Houses resolver functions for GraphQL queries and mutations.
- `queries/`: A directory for query examples or related scripts.
- `requirements.txt`: Lists the dependencies required for the project.

## Getting Started

### Installation

Follow these steps to set up and run the project locally:


Install virtualenv via pipx

If you specifically want to use virtualenv, you can use pipx, which is Homebrew’s recommended way to manage Python applications.

Install pipx if this is brew managed python:

    brew install pipx

Ensure pipx is configured:

    pipx ensurepath

Install virtualenv using pipx:

    pipx install virtualenv

Create a virtual environment using virtualenv:

    virtualenv .venv

Activate the virtual environment:

    source .venv/bin/activate

    # or deactivate when done
    deactivate

Proceed to install packages (e.g., Flask):

    pip install -r requirements.txt
    pip list

Or install manually:

    pip install 'strawberry-graphql[debug-server]'
    pip install fastapi uvicorn
    pip freeze > requirements.txt
    pip list

### Run the service:

    uvicorn main:app --reload

GraphGL server:
- http://127.0.0.1:8000/graphql

Example:

```commandline
   POST http://127.0.0.1:8000/graphql
   
   query {
       allBooks {
           id
           title
           author
           description
       }
   }



    POST http://127.0.0.1:8000/graphql
    
    query {
        getBookById(id: 1) {
            title
            author
        }
    }
   
   
    POST http://127.0.0.1:8000/graphql
    
    mutation {
        addBook(title: "The Great Gatsby", author: "F. Scott Fitzgerald", description: "A classic novel.") {
            id
            title
        }
    }

```

### Example Queries

You can find example queries in the `queries/` folder to test with your GraphQL server.

### Swagger docs

- http://127.0.0.1:8000/redoc#
- http://127.0.0.1:8000/docs#/


