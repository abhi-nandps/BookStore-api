from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    category: str
    description: str
    price: str  # Price stored as a string for the sake of simplicity in this example

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None

books_data = [
    {"id": 1, "title": "Dracula", "author": "Bram Stoker", "category": "Horror", "description": "Classic horror novel.", "price": "$9.99"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "category": "Drama", "description": "Romantic drama.", "price": "$12.99"},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Storybook", "description": "Fantasy adventure.", "price": "$15.99"},
    {"id": 4, "title": "Cinderella", "author": "Charles Perrault", "category": "Fairytale", "description": "Classic fairytale.", "price": "$7.99"},
    {"id": 5, "title": "Steve Jobs", "author": "Walter Isaacson", "category": "Biography", "description": "Biography of Steve Jobs.", "price": "$20.99"},
    {"id": 6, "title": "Encyclopedia Britannica", "author": "Various", "category": "Encyclopedia", "description": "Comprehensive encyclopedia.", "price": "$100.00"},
    {"id": 7, "title": "The Science Book", "author": "DK", "category": "Science", "description": "Science concepts explained.", "price": "$25.00"},
    {"id": 8, "title": "The Art of War", "author": "Sun Tzu", "category": "Strategy", "description": "Ancient Chinese military treatise.", "price": "$10.99"},
    {"id": 9, "title": "1984", "author": "George Orwell", "category": "Dystopian", "description": "Dystopian social science fiction.", "price": "$14.99"},
    {"id": 10, "title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Drama", "description": "Pulitzer Prize-winning novel.", "price": "$11.99"},
    {"id": 11, "title": "Frankenstein", "author": "Mary Shelley", "category": "Horror", "description": "Classic gothic novel.", "price": "$8.99"},
    {"id": 12, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "category": "Fantasy", "description": "First book in the Harry Potter series.", "price": "$9.99"},
    {"id": 13, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Fiction", "description": "Novel about teenage rebellion.", "price": "$10.99"},
    {"id": 14, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Classic", "description": "Novel set in the Jazz Age.", "price": "$10.99"},
    {"id": 15, "title": "Moby Dick", "author": "Herman Melville", "category": "Adventure", "description": "Epic sea story.", "price": "$12.99"},
    {"id": 16, "title": "War and Peace", "author": "Leo Tolstoy", "category": "Historical Fiction", "description": "Novel set during the Napoleonic Wars.", "price": "$15.99"},
    {"id": 17, "title": "The Odyssey", "author": "Homer", "category": "Epic", "description": "Ancient Greek epic poem.", "price": "$13.99"},
    {"id": 18, "title": "Hamlet", "author": "William Shakespeare", "category": "Drama", "description": "Shakespearean tragedy.", "price": "$8.99"},
    {"id": 19, "title": "The Iliad", "author": "Homer", "category": "Epic", "description": "Ancient Greek epic poem.", "price": "$13.99"},
    {"id": 20, "title": "A Brief History of Time", "author": "Stephen Hawking", "category": "Science", "description": "Introduction to cosmology.", "price": "$18.99"},
    {"id": 21, "title": "The Diary of a Young Girl", "author": "Anne Frank", "category": "Biography", "description": "Diary of Anne Frank during WWII.", "price": "$9.99"},
    {"id": 22, "title": "The Divine Comedy", "author": "Dante Alighieri", "category": "Classic", "description": "Epic poem about the afterlife.", "price": "$11.99"},
    {"id": 23, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "category": "Classic", "description": "Russian novel about morality.", "price": "$14.99"},
    {"id": 24, "title": "The Alchemist", "author": "Paulo Coelho", "category": "Adventure", "description": "Novel about a shepherd's journey.", "price": "$9.99"},
    {"id": 25, "title": "The Art of Computer Programming", "author": "Donald Knuth", "category": "Programming", "description": "Comprehensive book on algorithms.", "price": "$199.99"},
    {"id": 26, "title": "The Elements of Style", "author": "William Strunk Jr.", "category": "Writing", "description": "Guide to writing style.", "price": "$9.99"},
    {"id": 27, "title": "The Road", "author": "Cormac McCarthy", "category": "Post-Apocalyptic", "description": "Novel set in a post-apocalyptic world.", "price": "$12.99"},
    {"id": 28, "title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "category": "Children's", "description": "Philosophical story for children.", "price": "$7.99"},
    {"id": 29, "title": "A Game of Thrones", "author": "George R.R. Martin", "category": "Fantasy", "description": "First book in the A Song of Ice and Fire series.", "price": "$14.99"},
    {"id": 30, "title": "The Wind-Up Bird Chronicle", "author": "Haruki Murakami", "category": "Fiction", "description": "Novel about a Tokyo man's search for his wife.", "price": "$16.99"},
    {"id": 31, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy", "description": "Epic high-fantasy novel.", "price": "$29.99"},
    {"id": 32, "title": "The Shining", "author": "Stephen King", "category": "Horror", "description": "Horror novel set in an isolated hotel.", "price": "$14.99"},
    {"id": 33, "title": "Catch-22", "author": "Joseph Heller", "category": "Satire", "description": "Satirical novel set during WWII.", "price": "$13.99"},
    {"id": 34, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "category": "Philosophical", "description": "Philosophical novel about beauty.", "price": "$10.99"},
    {"id": 35, "title": "Jane Eyre", "author": "Charlotte Brontë", "category": "Romance", "description": "Gothic romance novel.", "price": "$12.99"},
    {"id": 36, "title": "The Name of the Wind", "author": "Patrick Rothfuss", "category": "Fantasy", "description": "First book in The Kingkiller Chronicle.", "price": "$15.99"},
    {"id": 37, "title": "The Fault in Our Stars", "author": "John Green", "category": "Young Adult", "description": "Young adult romance novel.", "price": "$9.99"},
    {"id": 38, "title": "Life of Pi", "author": "Yann Martel", "category": "Adventure", "description": "Adventure novel about survival.", "price": "$11.99"},
    {"id": 39, "title": "The Martian", "author": "Andy Weir", "category": "Science Fiction", "description": "Sci-fi novel about survival on Mars.", "price": "$14.99"},
    {"id": 40, "title": "Gone Girl", "author": "Gillian Flynn", "category": "Thriller", "description": "Psychological thriller.", "price": "$12.99"},
    {"id": 41, "title": "The Girl on the Train", "author": "Paula Hawkins", "category": "Mystery", "description": "Psychological thriller.", "price": "$10.99"},
    {"id": 42, "title": "Brave New World", "author": "Aldous Huxley", "category": "Dystopian", "description": "Dystopian novel about a controlled society.", "price": "$10.99"},
    {"id": 43, "title": "Slaughterhouse-Five", "author": "Kurt Vonnegut", "category": "Science Fiction", "description": "Sci-fi novel about WWII.", "price": "$9.99"},
    {"id": 44, "title": "The Handmaid's Tale", "author": "Margaret Atwood", "category": "Dystopian", "description": "Dystopian novel about a totalitarian society.", "price": "$12.99"},
    {"id": 45, "title": "The Book Thief", "author": "Markus Zusak", "category": "Historical Fiction", "description": "Novel set during WWII.", "price": "$11.99"},
    {"id": 46, "title": "The Chronicles of Narnia", "author": "C.S. Lewis", "category": "Fantasy", "description": "Fantasy novel series.", "price": "$24.99"},
    {"id": 47, "title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "History", "description": "Historical account of human evolution.", "price": "$18.99"},
    {"id": 48, "title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "category": "Psychology", "description": "Book about human thought processes.", "price": "$16.99"},
    {"id": 49, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "category": "Classic", "description": "Philosophical novel about family.", "price": "$14.99"},
    {"id": 50, "title": "The Old Man and the Sea", "author": "Ernest Hemingway", "category": "Adventure", "description": "Novel about an old fisherman's struggle.", "price": "$9.99"}
]


@app.get("/books", response_model=List[Book])
async def get_books():
    return books_data

@app.get("/books/category/{category}", response_model=List[Book])
async def get_books_by_category(category: str):
    filtered_books = [book for book in books_data if book['category'].lower() == category.lower()]
    if not filtered_books:
        raise HTTPException(status_code=404, detail="Books not found")
    return filtered_books

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books_data:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_update: BookUpdate):
    for book in books_data:
        if book["id"] == book_id:
            if book_update.title is not None:
                book["title"] = book_update.title
            if book_update.author is not None:
                book["author"] = book_update.author
            if book_update.category is not None:
                book["category"] = book_update.category
            if book_update.description is not None:
                book["description"] = book_update.description
            if book_update.price is not None:
                book["price"] = book_update.price
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
async def add_book(book: Book):
    # Check if the book ID already exists
    for b in books_data:
        if b["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")

    books_data.append(book.dict())
    return book

@app.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: int):
    global books_data
    for book in books_data:
        if book["id"] == book_id:
            books_data = [b for b in books_data if b["id"] != book_id]
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/author/{author_name}", response_model=List[Book])
async def get_books_by_author(author_name: str):
    filtered_books = [book for book in books_data if author_name.lower() in book["author"].lower()]

    if not filtered_books:
        raise HTTPException(status_code=404, detail="No books found by the given author")

    return filtered_books


@app.get("/books/price/{price}", response_model=List[Book])
async def get_books_by_price(price: float):
    filtered_books = [book for book in books_data if float(book["price"].replace("$", "")) == price]

    if not filtered_books:
        raise HTTPException(status_code=404, detail="No books found at the specified price")

    return filtered_books