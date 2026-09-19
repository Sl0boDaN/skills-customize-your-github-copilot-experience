from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Mergington Book Catalog API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


@app.get("/books")
def list_books():
    """Return all books in the catalog."""
    pass


@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    """Add a book to the catalog and return it."""
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book by ID, or a 404 when it is missing."""
    pass


# Start the server with:
# uvicorn starter-code:app --reload
