from fastapi import FastAPI
app = FastAPI(
    title="Library Management API",
    description="API quản lý thư viện",
    version="1.0.0"
)

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Learning SQL",
        "author": "Le Thi C",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Java Programming",
        "author": "Pham Van D",
        "category": "programming",
        "year": 2019,
        "is_available": False
    }
]

@app.get("/")
def get_books():
    return {"messenger" : "Welcome to Library Management API"}

@app.get("/books/available")
def get_book_avai():
    avai_books = []
    for book in books:
        if book["is_available"]== True:
            avai_books.append(book)
    return avai_books
@app.get("/books/available")
def get_book_avai():
    avai_books = []
    for book in books:
        if book["is_available"]== False:
            avai_books.append(book)
    return avai_books