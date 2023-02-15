from User import User

class Faculty(User):
    def __init__(self, username, password, designation, subject):
        User.__init__(User,username,password)
        self.__designation = designation
        self.__subject = subject

    @property
    def designation(self):
        return self.__designation
    @property
    def subject(self):
        return self.__subject

    @designation.setter
    def designation(self, designation):
        self.__designation = designation
    @subject.setter
    def subject(self, subject):
        self.__subject = subject