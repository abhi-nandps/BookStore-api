from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str  # Corrected from 'string' to 'str'
    author: str  # Corrected from 'string' to 'str'
    category: str  # Corrected from 'string' to 'str'
    description: str  # Corrected from 'string' to 'str'
    price: float
