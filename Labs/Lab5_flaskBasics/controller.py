from contact import  Contact
from db import DBHandler
from exceptions import *

class ContactController:
    def __init__(self):
        self.dbObj = DBHandler("localhost","root","Abcd1234","fcit")

    def addContact(self, name, mobileno,city,profession):
        flag = False
        try:
            contacts = self.dbObj.getAllContacts()
            if name == "" or mobileno == "" or city == "" or profession == "":
                raise NullValueNotAllowed()
            for contact in contacts:
                if contact.name == name:
                    raise NameAlreadyExists("Can't add two contacts for same name")
            for i in range(len(mobileno)):
                if (mobileno[i] < '0' or mobileno[i] > '9') and mobileno[i] != '+':
                    raise InvalidMobileNo("Invalid mobile number entered")
            flag = self.dbObj.createContact(Contact(name,mobileno,city,profession))
        except Exception as e:
            print(str(e))
        finally:
            return flag

    def getAllContacts(self):
        return self.dbObj.getAllContacts()

    def getContact(self, name):
        return self.dbObj.getContact(name)

    def validateUser(self, email, password):
        if len(password) < 8:
            return False
        if self.dbObj.isUserPresent(email):
            return False

        return self.insertUser(email,password)

    def insertUser(self, email, password):
        return self.dbObj.insertUser(email,password)

    def isUserPresent(self,email):
        return self.dbObj.isUserPresent(email)

    def authorize(self,email,password):
        return self.dbObj.authorize(email,password)