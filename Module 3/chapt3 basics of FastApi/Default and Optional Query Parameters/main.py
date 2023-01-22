from fastapi import FastAPI
from typing import Optional

app = FastAPI()

#DEFAULT QUERY PARAMETERS:
course_items = [{"course_name": "Python"}, {"course_name": "NodeJS"}, {"course_name": "Machine Learning"}]

@app.get("/courses/")
def read_courses(start: int = 0, end: int = 10):
    return course_items[start : start + end]


#OPTIONAL QUERY PARAMETERS:
course_items2 = {1: "Python", 2: "NodeJS", 3: "Machine Learning"}

@app.get("/courses2/{course_id}")
def read_courses2(course_id: int, q: Optional[str] = None):
    if q is not None:
        return {"course_name": course_items[course_id], "q": q} 
    return {"course_name": course_items[course_id]}


