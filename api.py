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
from db import DB
# Programe
db=DB()

@app.get("/seedDB")
def seed_db():
    
    
    # //add 3 prog
    # ramm
    p1=Program(db,fields={"id":"1","name":"BSCS","description":"Bechelar","start_date":"2022-02-02","end_date":"2023-02-03"})
    p1.insert()
    
    p2=Program(db,fields={"id":"2","name":"MSCS","description":"Masters","start_date":"2023-02-02","end_date":"2024-02-03"})
    p2.insert()

    
    p3=Program(db,fields={"id":"3","name":"PHD","description":"Post Diploma","start_date":"2024-02-02","end_date":"2025-02-03"})
    p3.insert()
    
    s1=Student(db,fields={"id":"1","name":"Ali","email":"ali@gmail.com","programme_id":"1"})
    s1.insert()
    
    s1=Student(db,fields={"id":"2","name":"Hamza","email":"hamzagmail.com","programme_id":"1"})
    s1.insert()
    
    s1=Student(db,fields={"id":"3","name":"Raza","email":"raza@gmail.com","programme_id":"1"})
    s1.insert()

    c1=Course(db,fields={"id":"1","name":"programming","description":"","start_date":"2022-01-02","end_date":"2022-02-03","programme_id":"1"})
    c1.insert()
    
    c2=Course(db,fields={"id":"2","name":"data science","description":"","start_date":"2022-01-02","end_date":"2022-02-03","programme_id":"1"})
    c2.insert()
    
    c3=Course(db,fields={"id":"3","name":"algorithms","description":"","start_date":"2022-01-02","end_date":"2022-02-03","programme_id":"1"})
    c3.insert()
    
    t1=Teacher(db,fields={"id":"1","name":"Nazia","email":"nazia@gmail.com","course_id":"1"})
    t1.insert()
    
    t2=Teacher(db,fields={"id":"2","name":"Saria","email":"saria@gmail.com","course_id":"2"})
    t2.insert()
    
    t3=Teacher(db,fields={"id":"3","name":"Saleem","email":"saleem@gmail.com","course_id":"3"})
    t3.insert()

    a1=Assignment(db,fields={"id":"1","name":"Assignment 1","description":"python","start_date":"2022-03-05","end_date":"2022-03-04","course_id":"2"}) 
    a1.insert()

    a2=Assignment(db,fields={"id":"2","name":"Assignment 2","description":"data science","start_date":"2022-03-05","end_date":"2022-03-04","course_id":"2"}) 
    a2.insert()
    
    a3=Assignment(db,fields={"id":"3","name":"Assignment 3","description":"pysocs","start_date":"2022-03-05","end_date":"2022-03-04","course_id":"2"}) 
    a3.insert()

    sc1=StudentCourse(db,fields={"id":"1","student_id":"1","course_id":"1"})
    sc1.insert()

    sc2=StudentCourse(db,fields={"id":"2","student_id":"1","course_id":"2"})
    sc2.insert()

    sc3=StudentCourse(db,fields={"id":"3","student_id":"1","course_id":"3"})

    sc1=StudentCourse(db,fields={"id":"4","student_id":"2","course_id":"1"})
    sc1.insert()

    sc2=StudentCourse(db,fields={"id":"5","student_id":"2","course_id":"2"})
    sc2.insert()

    sc3=StudentCourse(db,fields={"id":"6","student_id":"2","course_id":"3"})

    sc1=StudentCourse(db,fields={"id":"7","student_id":"3","course_id":"1"})
    sc1.insert()

    sc2=StudentCourse(db,fields={"id":"8","student_id":"3","course_id":"2"})
    sc2.insert()

    sc3=StudentCourse(db,fields={"id":"9","student_id":"3","course_id":"3"})
    sc3.insert()

    return "successfully seeded"

@app.get("/programme/{id}")
def get_programme_by_id(id: int):
    
    prog=Program(db,id=id)
    return prog.get()

@app.get("/all_programme")
def get_programme_by_id():
    
    return Program.getAll()


@app.post("/programme_insert")
def create_programme(fields:str):
    
    
    fields=eval(fields)
    prog=Program(db,fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/programme_update")
def update_programme(id:int,fields:str):
    fields=eval(fields)
    
    prog=Program(db,id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/programme_delete")
def delete_programme(id:int):
    
    prog=Program(db,id=id)
    prog.delete()
    return "Successfully deleted"

# Student
@app.get("/student/{id}")
def get_student_by_id(id: int):
    
    prog=Student(db,id=id)
    return prog.get()

@app.get("/all_student")
def get_student_by_id():
    return Student.getAll()


@app.post("/student_insert")
def create_student(fields:str):
    
    fields=eval(fields)
    prog=Student(db,fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/student_update")
def update_student(id:int,fields:str):
    fields=eval(fields)
    
    prog=Student(db,id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/student_delete")
def delete_student(id:int):
    
    prog=Student(db,id=id)
    prog.delete()
    return "Successfully deleted"


# Course
@app.get("/course/{id}")
def get_course_by_id(id: int):
    
    prog=Course(db,id=id)
    return prog.get()

@app.get("/all_course")
def get_course_by_id():
    return Course.getAll()


@app.post("/course_insert")
def create_course(fields:str):
    
    fields=eval(fields)
    prog=Course(db,fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/course_update")
def update_course(id:int,fields:str):
    
    fields=eval(fields)
    prog=Course(db,id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/course_delete")
def delete_course(id:int):
    
    prog=Course(db,id=id)
    prog.delete()
    return "Successfully deleted"



# Teacher

@app.get("/teacher/{id}")
def get_teacher_by_id(id: int):
    
    prog=Teacher(db,id=id)
    return prog.get()

@app.get("/all_teacher")
def get_teacher_by_id():
    return Teacher.getAll()


@app.post("/teacher_insert")
def create_teacher(fields:str):
    
    fields=eval(fields)
    prog=Teacher(db,fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/teacher_update")
def update_teacher(id:int,fields:str):
    
    fields=eval(fields)
    prog=Teacher(db,id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/teacher_delete")
def delete_teacher(id:int):
    
    prog=Teacher(db,id=id)
    prog.delete()
    return "Successfully deleted"


# Assignment

@app.get("/assignment/{id}")
def get_assignment_by_id(id: int):
    
    prog=Assignment(db,id=id)
    return prog.get()

@app.get("/all_assignment")
def get_assignment_by_id():
    return Assignment.getAll()


@app.post("/assignment_insert")
def create_assignment(fields:str):
    
    fields=eval(fields)
    prog=Assignment(db,fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/assignment_update")
def update_assignment(id:int,fields:str):
    fields=eval(fields)
    
    prog=Assignment(db,id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/assignment_delete")
def delete_assignment(id:int):
    
    prog=Assignment(db,id=id)
    prog.delete()
    return "Successfully deleted"


# StudentCourse

@app.get("/student_course/{id}")
def get_student_course_by_id(id: int):
    
    prog=StudentCourse(db,id=id)
    return prog.get()

@app.get("/all_student_course")
def get_student_course_by_id():
    return StudentCourse.getAll()


@app.post("/student_course_insert")
def create_student_course(fields:str):
    
    fields=eval(fields)
    prog=StudentCourse(db,fields=fields)
    prog.insert()
    return "Successfully created"


@app.put("/student_course_update")
def update_student_course(id:int,fields:str):
    fields=eval(fields)
    
    prog=StudentCourse(db,id=id)
    prog.update(update=fields)
    return "Successfully updated"


@app.delete("/student_course_delete")
def delete_student_course(id:int):
    
    prog=StudentCourse(db,id=id)
    prog.delete()
    return "Successfully deleted"


