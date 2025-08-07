from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Attendance(BaseModel):
    student_id: str
    name: str
    status: str

# Dummy data
attendance_data = [
    {"student_id": "1", "name": "Ali", "status": "Present"},
    {"student_id": "2", "name": "Ahmed", "status": "Absent"},
    {"student_id": "3", "name": "Sara", "status": "Present"},
]

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.get("/attendance", response_model=List[Attendance])
def get_attendance():
    return attendance_data
