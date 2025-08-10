# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Optional

# app = FastAPI()

# class Attendance(BaseModel):
#     date: str
#     student_id: str
#     name: str
#     status: str

# # Dummy data
# attendance_data = [
#     {"date": "1-08-2025", "student_id": "1", "name": "Ali", "status": "Present"},
#     {"date": "1-08-2025", "student_id": "2", "name": "Ahmed", "status": "Absent"},
#     {"date": "1-08-2025", "student_id": "3", "name": "Sara", "status": "Present"},
# ]

# @app.get("/")
# def read_root():
#     return {"message": "API is working"}

# @app.get("/attendance", response_model=List[Attendance])
# def get_attendance():
#     return attendance_data


# @app.get("/attendance/{student_id}", response_model=Optional[Attendance])
# def get_single_attendance(student_id: str):
#     # Find the single record that matches the student_id
#     for record in attendance_data:
#         if record["student_id"] == student_id:
#             return record
    
#     # If no matching record is found, return a 404 Not Found error
#     raise HTTPException(status_code=404, detail="Student not found")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware # Import the CORSMiddleware

app = FastAPI()

# Add the CORS middleware
# This is crucial for your Flutter web app to communicate with your backend
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Use ["*"] to allow all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Attendance(BaseModel):
    date: str
    student_id: str
    name: str
    status: str


# Dummy data
attendance_data = [
    {"date": "08-08-2025", "student_id": "910", "name": "waqar", "status": "Present"},
    {"date": "07-08-2025", "student_id": "910", "name": "waqar", "status": "Absent"},
    {"date": "08-06-2025", "student_id": "910", "name": "waqar", "status": "Absent"},
    {"date": "08-05-2025", "student_id": "910", "name": "waqar", "status": "Present"},
    {"date": "08-04-2025", "student_id": "910", "name": "waqar", "status": "Present"},

    {"date": "08-08-2025", "student_id": "7767", "name": "waqas", "status": "Present"},
    {"date": "08-07-2025", "student_id": "7767", "name": "waqas", "status": "Absent"},
    {"date": "08-06-2025", "student_id": "7767", "name": "waqas", "status": "Present"},
]


@app.get("/")
def read_root():
    return {"message": "API is working"}


@app.get("/attendance", response_model=List[Attendance])
def get_attendance():
    return attendance_data




@app.get("/attendance/{student_id}", response_model=List[Attendance])
def get_single_attendance(student_id: str):

    matching_records = []
    
    for record in attendance_data:
        if record["student_id"] == student_id:
            matching_records.append(record)
    if not matching_records:
        raise HTTPException(status_code=404, detail="Student not found")
        
    return matching_records