from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import dependencies
import schemas

router = APIRouter()

@router.post("/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_author(db=db, author=author)

@router.get("/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    return crud.get_authors(db, skip=skip, limit=limit)

@router.get("/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(dependencies.get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@router.delete("/{author_id}", response_model=dict)
def delete_author(author_id: int, db: Session = Depends(dependencies.get_db)):
    db_author = crud.delete_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}