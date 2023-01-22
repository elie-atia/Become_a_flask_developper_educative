from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Course(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    author: Optional[str] = None

app = FastAPI()

@app.post("/courses/")
def create_course(course: Course):
    return course
