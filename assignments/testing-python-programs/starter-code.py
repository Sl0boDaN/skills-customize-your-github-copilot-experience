from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Mergington Book Catalog API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


def find_book(book_id):
    """Return a book by ID, or None when it is not in the catalog."""
    return next((book for book in books if book["id"] == book_id), None)


def format_book(book):
    """Return a readable display string for a book."""
    return f'{book["title"]} by {book["author"]}'


def add_book(title, author):
    """Add a book with the next available integer ID."""
    next_id = max((book["id"] for book in books), default=0) + 1
    book = {"id": next_id, "title": title, "author": author}
    books.append(book)
    return book


@app.get("/books")
def list_books():
    return books


@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    return add_book(book.title, book.author)


@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = find_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
