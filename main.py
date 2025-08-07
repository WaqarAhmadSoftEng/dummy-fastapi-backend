from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Attendance(BaseModel):
    date: str
    student_id: str
    name: str
    status: str

# Dummy data
attendance_data = [
    {"date": "1-08-2025", "student_id": "1", "name": "Ali", "status": "Present"},
    {"date": "1-08-2025", "student_id": "2", "name": "Ahmed", "status": "Absent"},
    {"date": "1-08-2025", "student_id": "3", "name": "Sara", "status": "Present"},
]

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.get("/attendance", response_model=List[Attendance])
def get_attendance():
    return attendance_data


@app.get("/attendance/{student_id}", response_model=Optional[Attendance])
def get_single_attendance(student_id: str):
    # Find the single record that matches the student_id
    for record in attendance_data:
        if record["student_id"] == student_id:
            return record
    
    # If no matching record is found, return a 404 Not Found error
    raise HTTPException(status_code=404, detail="Student not found")
