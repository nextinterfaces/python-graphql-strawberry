from typing import List
import strawberry
from models import Book

# Mock database
BOOKS_DB = [
    Book(id=1, title="1984", author="George Orwell", description="Dystopian novel."),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="Classic novel."),
]

@strawberry.type
class Query:
    @strawberry.field
    def all_books(self) -> List[Book]:
        return BOOKS_DB

    @strawberry.field
    def get_book_by_id(self, id: int) -> Book:
        for book in BOOKS_DB:
            if book.id == id:
                return book
        raise ValueError(f"Book with ID {id} not found.")

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str, description: str) -> Book:
        new_book = Book(
            id=len(BOOKS_DB) + 1,
            title=title,
            author=author,
            description=description,
        )
        BOOKS_DB.append(new_book)
        return new_book
