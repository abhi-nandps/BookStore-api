from typing import List
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    category: str
    description: str
    price: float
