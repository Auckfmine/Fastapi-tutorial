from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
import database

class Author(database.Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio = Column(Text, nullable=True)


#TASK1 : COMPLETER LES MODELES DE CATEGORY ET BOOK 