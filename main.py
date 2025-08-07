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
    {"date": "1-08-2025", "id": "1", "name": "Ali", "status": "Present"},
    {"date": "1-08-2025", "id": "2", "name": "Ahmed", "status": "Absent"},
    {"date": "1-08-2025", "id": "3", "name": "Sara", "status": "Present"},
]

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.get("/attendance", response_model=List[Attendance])
def get_attendance():
    return attendance_data
