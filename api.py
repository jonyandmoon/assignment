from typing import Dict
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from models import Program
from models import Student
from models import Course
from models import Teacher
from models import Assignment
from models import StudentCourse
app = FastAPI()

# Programe
@app.get("/programme/{id}")
def get_programme_by_id(id: int):
    prog=Program(id=id)
    return prog.get()

@app.get("/all_programme")
def get_programme_by_id():
    return Program.getAll()


@app.post("/programme_insert")
def create_programme(fields:str):
    fields=eval(fields)
    prog=Program(fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/programme_update")
def update_programme(id:int,fields:str):
    fields=eval(fields)
    prog=Program(id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/programme_delete")
def delete_programme(id:int):
    prog=Program(id=id)
    prog.delete()
    return "Successfully deleted"

# Student
@app.get("/student/{id}")
def get_student_by_id(id: int):
    prog=Student(id=id)
    return prog.get()

@app.get("/all_student")
def get_student_by_id():
    return Student.getAll()


@app.post("/student_insert")
def create_student(fields:str):
    fields=eval(fields)
    prog=Student(fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/student_update")
def update_student(id:int,fields:str):
    fields=eval(fields)
    prog=Student(id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/student_delete")
def delete_student(id:int):
    prog=Student(id=id)
    prog.delete()
    return "Successfully deleted"


# Course
@app.get("/course/{id}")
def get_course_by_id(id: int):
    prog=Course(id=id)
    return prog.get()

@app.get("/all_course")
def get_course_by_id():
    return Course.getAll()


@app.post("/course_insert")
def create_course(fields:str):
    fields=eval(fields)
    prog=Course(fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/course_update")
def update_course(id:int,fields:str):
    fields=eval(fields)
    prog=Course(id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/course_delete")
def delete_course(id:int):
    prog=Course(id=id)
    prog.delete()
    return "Successfully deleted"



# Teacher

@app.get("/teacher/{id}")
def get_teacher_by_id(id: int):
    prog=Teacher(id=id)
    return prog.get()

@app.get("/all_teacher")
def get_teacher_by_id():
    return Teacher.getAll()


@app.post("/teacher_insert")
def create_teacher(fields:str):
    fields=eval(fields)
    prog=Teacher(fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/teacher_update")
def update_teacher(id:int,fields:str):
    fields=eval(fields)
    prog=Teacher(id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/teacher_delete")
def delete_teacher(id:int):
    prog=Teacher(id=id)
    prog.delete()
    return "Successfully deleted"


# Assignment

@app.get("/assignment/{id}")
def get_assignment_by_id(id: int):
    prog=Assignment(id=id)
    return prog.get()

@app.get("/all_assignment")
def get_assignment_by_id():
    return Assignment.getAll()


@app.post("/assignment_insert")
def create_assignment(fields:str):
    fields=eval(fields)
    prog=Assignment(fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/assignment_update")
def update_assignment(id:int,fields:str):
    fields=eval(fields)
    prog=Assignment(id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/assignment_delete")
def delete_assignment(id:int):
    prog=Assignment(id=id)
    prog.delete()
    return "Successfully deleted"


# StudentCourse

@app.get("/student_course/{id}")
def get_student_course_by_id(id: int):
    prog=StudentCourse(id=id)
    return prog.get()

@app.get("/all_student_course")
def get_student_course_by_id():
    return StudentCourse.getAll()


@app.post("/student_course_insert")
def create_student_course(fields:str):
    fields=eval(fields)
    prog=StudentCourse(fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/student_course_update")
def update_student_course(id:int,fields:str):
    fields=eval(fields)
    prog=StudentCourse(id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/student_course_delete")
def delete_student_course(id:int):
    prog=StudentCourse(id=id)
    prog.delete()
    return "Successfully deleted"


