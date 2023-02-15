from Faculty import Faculty
from Student import Student
from Model import DBHandler

def register_faculty(username,password,designation,subject):
    faculty = Faculty(username,password,designation,subject)
    mydb = DBHandler("localhost","root","Abcd1234","fcit")      # initiate connection with database
    return mydb.register_faculty(faculty)

def register_student(username,password,semester,cgpa,major):
    student = Student(username,password,semester,cgpa,major)
    mydb = DBHandler("localhost","root","Abcd1234","fcit")
    return mydb.register_student(student)

def authenticate_faculty(username,password):
    mydb = DBHandler("localhost","root","Abcd1234","fcit")
    fac = mydb.get_faculty(username,password)
    return fac

def authenticate_student(username,password):
    mydb = DBHandler("localhost","root","Abcd1234","fcit")
    std = mydb.get_student(username,password)
    return std

def update_student(username,password,semester,cgpa,major):
    student = Student(username, password, semester, cgpa, major)
    mydb = DBHandler("localhost", "root", "Abcd1234", "fcit")
    return mydb.update_student(student)

def update_faculty(username,password,designation,subject):
    faculty = Faculty(username,password,designation,subject)
    mydb = DBHandler("localhost","root","Abcd1234","fcit")
    return mydb.update_faculty(faculty)

def delete_faculty(id):
    mydb = DBHandler("localhost", "root", "Abcd1234", "fcit")
    return mydb.delete_faculty(id)

def delete_student(id):
    mydb = DBHandler("localhost", "root", "Abcd1234", "fcit")
    return mydb.delete_student(id)