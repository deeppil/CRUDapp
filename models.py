from pydantic import BaseModel
from typing import Optional

# Input model for creating a post (CREATE)
class StudentCreate(BaseModel):
    name: str
    roll_no: int
    branch: str
    year: int


# Input model for updating (UPDATE)
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    roll_no: Optional[int] = None
    branch: Optional[str] = None
    year: Optional[int] = None


# Output model for responses
class StudentResponse(BaseModel):
    id: str
    name: str
    roll_no: int
    branch: str
    year: int