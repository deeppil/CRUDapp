from fastapi import APIRouter, HTTPException
from models import StudentCreate, StudentUpdate
import crud

router = APIRouter()

@router.post("/students")
def create_student(student: StudentCreate):
    return crud.create_student(student.dict())

@router.get("/students")
def get_students():
    return crud.get_students()

@router.get("/students/{student_id}")
def get_student(student_id: str):
    student = crud.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/students/{student_id}")
def update_student(student_id: str, student: StudentUpdate):
    updated = crud.update_student(student_id, student.dict(exclude_unset=True))
    if updated == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"updated": True}

@router.delete("/students/{student_id}")
def delete_student(student_id: str):
    deleted = crud.delete_student(student_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"deleted": True}
