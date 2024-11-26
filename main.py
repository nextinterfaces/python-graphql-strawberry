from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry

from resolvers import Query, Mutation

# Create the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Create FastAPI app
app = FastAPI()

# Mount GraphQL route
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {"message": "Welcome to the Strawberry GraphQL API"}
