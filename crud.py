from bson import ObjectId
from database import student_collection

# CREATE
def create_student(student_data: dict):
    result = student_collection.insert_one(student_data)
    student_data["_id"] = str(result.inserted_id)
    return student_data


# READ
def get_students():
    students = []
    for student in student_collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    return students


# UPDATE
def update_student(student_id: str, updated_data: dict):
    result = student_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": updated_data}
    )
    return result.modified_count


# DELETE
def delete_student(student_id: str):
    result = student_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )
    return result.deleted_count
