
students_list = []

def addStudents(name,id):
    student={"name",name,"id",id}
    students_list.append(student)

def printStudents():
    for student in students_list:
        print(student)

decide=input("Do you want to enter student details: ")
if( not decide == "Yes"):
    quit()

name=input("Student Name: ")
id=input("Student id: ")

addStudents(name,id)
printStudents()
