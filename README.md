
# Python GraphQL Strawberry Examples

This repository demonstrates examples of using the [Strawberry GraphQL](https://strawberry.rocks/) library hosted on [FastAPI](https://fastapi.tiangolo.com/) service

GraphQL is a query language for APIs and a runtime for executing those queries. It allows clients to request only the data they need, making APIs more flexible and efficient.

### Core Concepts

- **Schema**: Defines the structure of your API, including types, queries, and mutations.
- **Query**: Fetch data from the server (similar to GET in REST).
- **Mutation**: Modify server-side data (similar to POST, PUT, DELETE in REST).
- **Resolvers**: Functions that resolve queries and mutations by returning data.
- **Types**: Define the shape of the data in your schema (e.g., String, Int, Boolean, Object).

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



# GraphQL: Pros and Cons

## **Pros (Advantages of GraphQL)**

1. **Flexible Data Retrieval**
    - Clients can request exactly the data they need and nothing more.
    - Reduces over-fetching (too much data) and under-fetching (insufficient data).

2. **Single Endpoint**
    - Unlike REST APIs, which often require multiple endpoints, GraphQL uses a single endpoint for all queries and mutations.

3. **Strongly Typed Schema**
    - GraphQL schemas are well-defined and provide clear documentation.
    - Enables robust type checking and ensures API consistency.

4. **Real-Time Capabilities**
    - Supports **subscriptions** for real-time updates, e.g., live feeds or notifications.

5. **Self-Documenting**
    - Tools like GraphQL Playground or Apollo Studio allow you to explore APIs interactively.
    - The schema itself serves as documentation.

6. **Reduced Versioning**
    - Schema evolution is easier with GraphQL since clients request only the fields they need.
    - New fields can be added without affecting existing clients.

7. **Efficient for Front-End Development**
    - Front-end teams can independently query the data they need without waiting for backend changes.
    - Perfect for microservices where data comes from multiple sources.

8. **Batching and Caching**
    - GraphQL can batch and cache requests (with tools like Apollo Client) to optimize performance.

---

## **Cons (Disadvantages of GraphQL)**

1. **Complexity in Setup and Maintenance**
    - GraphQL servers require careful schema design and resolver implementation.
    - Requires more upfront work compared to REST.

2. **Overhead in Simple Use Cases**
    - For straightforward APIs, REST may be simpler and faster to implement.
    - GraphQL’s flexibility can be overkill for small projects.

3. **Caching Challenges**
    - REST leverages HTTP caching (e.g., `ETag`, `304 Not Modified`) easily.
    - GraphQL caching is more complex and often requires client-side solutions like Apollo Cache.

4. **Performance Issues**
    - Flexible queries can lead to **expensive database calls** or overloading the server with deeply nested queries.
    - Tools like query complexity analysis are needed to mitigate this.

5. **Learning Curve**
    - Developers need to learn GraphQL syntax, concepts, and tools (e.g., Apollo, Relay).
    - Debugging can also be more challenging compared to REST.

6. **Client-Side Complexity**
    - Requires specialized clients (e.g., Apollo Client, Relay) for optimal use.
    - Managing queries and state can get complicated in large applications.

7. **Potential for Abuse**
    - Malicious users can craft overly complex queries, causing performance bottlenecks.
    - Requires query validation and rate limiting to prevent abuse.

8. **Tooling Dependency**
    - Heavily reliant on tooling (e.g., GraphQL servers, libraries).
    - Lacks native browser or HTTP support compared to REST.

9. **Not SEO-Friendly**
    - Unlike REST, GraphQL responses are JSON, which search engines cannot easily index.

---

## **When to Use GraphQL?**
- **Ideal For**:
    - Applications needing dynamic, flexible data fetching (e.g., SPAs or mobile apps).
    - Complex APIs with many data relationships.
    - Real-time applications needing subscriptions.

- **Not Ideal For**:
    - Simple, CRUD-like APIs.
    - Use cases where caching or SEO is critical.
    - Teams unfamiliar with GraphQL who may face a steep learning curve.



