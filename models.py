from MyBaseModel import MyBaseModel

class Program(MyBaseModel):
    table="programme"
    primary_key="id"
    fields=["id","name","description","start_date","end_date"]

class Student(MyBaseModel):
    table="student"
    primary_key="id"
    fields=["id","name","email","programme_id"]


class Course(MyBaseModel):
    table="course"
    primary_key="id"
    fields=["id","name","description","start_date","end_date","programme_id"]



class Teacher(MyBaseModel):
    table="teacher"
    primary_key="id"
    fields=["id","name","email","course_id"]


class Assignment(MyBaseModel):
    table="assignment"
    primary_key="id"
    fields=["id","name","description","start_date","end_date","course_id"]


class StudentCourse(MyBaseModel):
    table="student_course"
    primary_key="id"
    fields=["id","student_id","course_id"]

    