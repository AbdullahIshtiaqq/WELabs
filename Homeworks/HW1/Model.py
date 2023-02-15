from Faculty import Faculty
from Student import Student
from Exceptions import UserNotFound
from Exceptions import UserAlreadyExists
import pymysql

class DBHandler:
    def __init__(self, host, name, password, database):
        self.__host = host
        self.__name = name
        self.__password = password
        self.__database = database

    def register_faculty(self, faculty):
        mydb = None
        cursor = None
        returnVal = True    # value to return, returns true if faculty registered successfully
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__name, password=self.__password, database=self.__database)
            cursor = mydb.cursor()

            # checks if the username already exists, if it exists, throw exception
            query = "select username from User"
            cursor.execute(query)
            usernames = cursor.fetchall()

            for username in usernames:
                if username[0] == faculty.username:
                    raise UserAlreadyExists("Username already taken")

            # insert data into user table first
            query = "insert into User(username, password) values (%s,%s)"
            cursor.execute(query,(faculty.username,faculty.password))

            # get user id from user table
            query = "select id from User where username = %s and password = %s"
            cursor.execute(query,(faculty.username,faculty.password))
            myTuple = cursor.fetchone()
            user_id = myTuple[0]

            # insert data into faculty table
            query = "insert into Faculty(designation, subject,user_id) values (%s,%s,%s)"
            cursor.execute(query, (faculty.designation,faculty.subject,user_id))
            mydb.commit()       #commit to save changes
        except Exception as e:
            returnVal = False
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()
            return returnVal

    def register_student(self, student):
        mydb = None
        cursor = None
        returnVal = True
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__name, password=self.__password, database=self.__database)
            cursor = mydb.cursor()

            # checks if the username already exists, if it exists, throw exception
            query = "select username from User"
            cursor.execute(query)
            usernames = cursor.fetchall()

            for username in usernames:
                if username[0] == student.username:
                    raise UserAlreadyExists("Username already taken")

            # insert data into user table first
            query = "insert into User(username, password) values (%s,%s)"
            cursor.execute(query,(student.username,student.password))

            # get user id from user table
            query = "select id from User where username = %s and password = %s"
            cursor.execute(query, (student.username, student.password))
            myTuple = cursor.fetchone()
            user_id = myTuple[0]

            # insert data into faculty table
            query = "insert into Student(semester,cgpa,major,user_id) values (%s,%s,%s,%s)"
            cursor.execute(query, (student.semester, student.cgpa, student.major,user_id))
            mydb.commit()
        except Exception as e:
            returnVal = False
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()
            return returnVal

    def get_faculty(self, username, password):
        mydb = None
        cursor = None
        faculty = None      # variable to hold faculty object if data found in database
        fac_id = 0          # variable to hold faculty id
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__name, password=self.__password, database=self.__database)
            cursor = mydb.cursor()

            # get user id from user table
            query = "select id from User where username = %s and password = %s"
            cursor.execute(query,(username,password))
            myTuple = cursor.fetchone()

            # if user not found, raise exception
            if myTuple == None:
                raise UserNotFound("No user with this username and password found")
            user_id = myTuple[0]

            # select the faculty data from respective table
            query = "select designation, subject, id from Faculty where user_id = %s"
            cursor.execute(query, (user_id))
            myTuple = cursor.fetchone()

            # checks if the data was retrieved successfully
            # this can fail if the user table have id but there is no record linked to that id in faculty table
            if myTuple == None:
                raise UserNotFound("No user with this username and password found")

            faculty = Faculty(username,password,myTuple[0],myTuple[1])
            fac_id = myTuple[2]
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()
            return (faculty,fac_id)

    def get_student(self, username, password):
        mydb = None
        cursor = None
        student = None      # variable to hold student object if data found in database
        std_id = 0          # variable to hold student id
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__name, password=self.__password, database=self.__database)
            cursor = mydb.cursor()

            # get user id from user table
            query = "select id from User where username = %s and password = %s"
            cursor.execute(query,(username,password))
            myTuple = cursor.fetchone()

            # if user not found, raise exception
            if myTuple == None:
                raise UserNotFound("No user with this username and password found")
            user_id = myTuple[0]

            # select the student data from respective table
            query = "select semester,cgpa,major,id from Student where user_id = %s"
            cursor.execute(query, (user_id))
            myTuple = cursor.fetchone()
            # checks if the data was retrieved successfully
            if myTuple == None:
                raise UserNotFound("No user with this username and password found")

            student = Student(username,password,myTuple[0],myTuple[1],myTuple[2])
            std_id = myTuple[3]
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()
            return (student,std_id)

    def update_faculty(self, faculty):
        mydb = None
        cursor = None
        returnVal = True
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__name, password=self.__password, database=self.__database)
            cursor = mydb.cursor()

            # get user id from user table
            query = "select id from User where username = %s and password = %s"
            cursor.execute(query,(faculty.username,faculty.password))
            myTuple = cursor.fetchone()

            # if data not found, raise exception
            if myTuple == None:
                raise UserNotFound("No user found with this data")
            user_id = myTuple[0]

            # update data
            query = "update Faculty set designation = %s, subject = %s where user_id = %s"
            cursor.execute(query, (faculty.designation,faculty.subject,user_id))
            mydb.commit()
        except Exception as e:
            returnVal = False
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()
            return returnVal

    def update_student(self, student):
        mydb = None
        cursor = None
        returnVal = True
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__name, password=self.__password, database=self.__database)
            cursor = mydb.cursor()

            # get id from user table
            query = "select id from User where username = %s and password = %s"
            cursor.execute(query,(student.username,student.password))
            myTuple = cursor.fetchone()

            # if username doesn't match in database, raise exception
            if myTuple == None:
                raise UserNotFound("No user found with this data")
            user_id = myTuple[0]

            #update data
            query = "update Student set semester = %s, cgpa = %s, major = %s where user_id = %s"
            cursor.execute(query, (student.semester,student.cgpa,student.major,user_id))
            mydb.commit()
        except Exception as e:
            returnVal = False
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()
            return returnVal

    def delete_faculty(self, id):
        mydb = None
        cursor = None
        returnVal = True
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__name, password=self.__password,
                                   database=self.__database)
            cursor = mydb.cursor()

            # get user id from faculty table ( because we need to delete data from user table too )
            query = "select user_id from Faculty where id = %s"
            cursor.execute(query, (id))
            myTuple = cursor.fetchone()

            # if id not present in faculty table, raise exception
            if myTuple == None:
                raise UserNotFound("No user with this id found")
            user_id = myTuple[0]

            # first delete from faculty
            query = "delete from Faculty where id = %s"
            cursor.execute(query, (id))

            # then delete from user table ( we can't delete from user table first as it is used as foreign key in other table )
            query = "delete from User where id = %s"
            cursor.execute(query, (user_id))
            mydb.commit()

        except Exception as e:
            returnVal = False
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()
            return returnVal

    def delete_student(self, id):
        mydb = None
        cursor = None
        returnVal = True
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__name, password=self.__password,
                                   database=self.__database)
            cursor = mydb.cursor()

            # get user id from user table ( because we need to delete data from user table too )
            query = "select user_id from Student where id = %s"
            cursor.execute(query, (id))
            myTuple = cursor.fetchone()
            # if id not present in student table, raise exception
            if myTuple == None:
                raise UserNotFound("No user with this id found")
            user_id = myTuple[0]

            # first delete from faculty
            query = "delete from Student where id = %s"
            cursor.execute(query, (id))

            # then delete from user table ( we can't delete from user table first as it is used as foreign key in other table )
            query = "delete from User where id = %s"
            cursor.execute(query, (user_id))
            mydb.commit()

        except Exception as e:
            returnVal = False
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()
            return returnVal