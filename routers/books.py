from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import dependencies
import schemas

router = APIRouter()

# TACHE 3 : COMPLETE LE ROUTING DE MODULE BOOKS
