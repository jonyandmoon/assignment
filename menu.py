from models import Program
from models import Student
from models import Course
from models import Teacher
from models import Assignment
from models import StudentCourse
from db import DB

db=DB()

mapper={1: "Program",
2: "Student",
3: "Course",
4: "Teacher",
5: "Assignment",
6: "StudentCourse"}

mappero={
    1: "Insert",
2: "Update",
3: "Delete",
4: "SelectId",
5: "SelectAll"
}
while(True):
    print(''' Select Table to update
    1. Program
    2. Student
    3. Course
    4. Teacher
    5. Assignment
    6. StudentCourse
    7. Exit
        ''')

    cls = int(input())


    if cls not in [1,2,3,4,5,6,7]:
        print("Invalid selection")
        continue
    elif(cls==7):
        break
    print(f''' Select Operation {mapper[cls]}
    1. Insert
    2. Update
    3. Delete
    4. Select by id
    5. Select all
    6. Exit
    7. Back
    ''')
    opp=int(input())

    if cls not in [1,2,3,4,5,6,7]:
        print("Invalid selection")
        continue
    elif(opp==6):
        break
    elif(opp==7):
        continue



    if cls==1 :
        if opp in [2,3,4]:
            
            print (f"Enter id for {mappero[opp]} of " + mapper[cls] )
            id=input()
            instance=eval(mapper[cls]+"(db,id="+id+")")
            if opp==2:
                print(f"Enter Data of {mapper[cls]} for update in Dictionary format")
                data=eval(input())
                instance.update(update=data)
                print("successfully updated")
            elif opp==3 :
                instance.delete()
                print("successfully deleted")
            else:
                print (instance.get())


        elif opp ==1:
            print(f"Enter Data of {mapper[cls]} in Dictionary format")
            data=eval(input())
            instance=eval(mapper[cls]+"(db)")
            instance.set_fields(data)
            instance.insert()
            print("Added Successfully")

        else:
            data=eval(mapper[cls]+".getAll()")
            print(data)
