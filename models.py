from typing import List
import strawberry

@strawberry.type
class Book:
    id: int
    title: str
    author: str
    description: str
