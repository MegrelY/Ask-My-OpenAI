from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    question: str  # Expecting a string

class QueryResponse(BaseModel):
    answer: str
    references: List[str]  # Assuming references are optional, you can set an empty list as default
