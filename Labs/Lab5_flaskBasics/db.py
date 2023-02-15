from contact import Contact
import pymysql

class DBHandler:
    def __init__(self, host, user, password, database):
        self.__mydb = None
        try:
            self.__mydb = pymysql.connect(host= host, user= user, password= password, database= database)
        except Exception as e:
            print(str(e))

    def __del__(self):
        if self.__mydb != None:
            self.__mydb.close()

    def createContact(self,contact):
        flag = False
        cursor = None
        try:
            cursor = self.__mydb.cursor()
            query = "insert into contacts (user_id,name, mobileno, city, profession) values (%s,%s,%s,%s,%s)"
            args = (78,contact.name, contact.mobileno, contact.city, contact.profession)
            cursor.execute(query,args)
            self.__mydb.commit()
            flag = True
        except Exception as e:
            print (str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag

    def getContact(self, name):
        contact = None
        cursor = None
        try:
            cursor = self.__mydb.cursor()
            query = "select mobileno,city,profession from contacts where name = %s"
            cursor.execute(query,(name))
            myTuple = cursor.fetchone()
            if myTuple != None:
                contact = Contact(name,myTuple[0],myTuple[1],myTuple[2])
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()
            return contact

    def getAllContacts(self):
        contacts = []
        cursor = None
        try:
            cursor = self.__mydb.cursor()
            query = "select  contact_id,name, mobileno, city, profession from contacts"
            cursor.execute(query)
            listOfTuples = cursor.fetchall()
            contacts = listOfTuples
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()
            return contacts

    def isUserPresent(self, email):
        flag = False
        try:
            cursor=self.__mydb.cursor()
            query="select email from contact_users"
            cursor.execute(query)
            results=cursor.fetchall()
            for mail in results:
                if mail[0] == email:
                    flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag

    def insertUser(self, email, password):
        flag= False
        cursor = None
        try:
            cursor = self.__mydb.cursor()
            query = "insert into contact_users(email, password) values(%s,%s)"
            args = (email,password)
            cursor.execute(query,args)
            flag = True
            self.__mydb.commit()
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag

    def authorize(self,email,password):
        flag = False
        cursor = None
        try:
            cursor = self.__mydb.cursor()
            query = "select password from contact_users where email=%s"
            cursor.execute(query,(email))
            result = cursor.fetchone()
            if result[0] == password:
                flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag