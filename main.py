from fastapi import FastAPI

import database
import models
from routers import authors, books, categories

app = FastAPI()

# Initialize the database
database.Base.metadata.create_all(bind=database.engine)

# Register routers
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
