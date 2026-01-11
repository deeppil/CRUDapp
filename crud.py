from bson import ObjectId
from database import student_collection

# CREATE - create a new student
def create_student(stud_data: dict):
    result = student_collection.insert_one(stud_data) 
    stud_data["_id"] = str(result.inserted_id) 
    return stud_data


# READ - read all students
def get_students():
    students = []
    for student in student_collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    return students 


# UPDATE - update a student using ID
def update_student(student_id: str, updated_data: dict):
    result = student_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": updated_data}
    )
    return result.modified_count


# DELETE - delete a student using ID
def delete_student(student_id: str):
    result = student_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )
    return result.deleted_count
