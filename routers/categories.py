from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import dependencies
import schemas

router = APIRouter()




#TACHE 4 : COMPLTEER LES ROUTES DE MODULE CATEGORIES