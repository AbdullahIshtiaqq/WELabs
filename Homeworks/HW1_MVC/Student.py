from User import User

class Student(User):
    def __init__(self,username,password,sem,cgpa,major):
        User.__init__(User,username,password)
        self.__semester = sem
        self.__cgpa = cgpa
        self.__major = major

    @property
    def semester(self):
        return self.__semester
    @property
    def cgpa(self):
        return self.__cgpa
    @property
    def major(self):
        return self.__major
    
    @semester.setter
    def semester(self, sem):
        self.__semester = sem
    @cgpa.setter
    def cgpa(self, cgpa):
        self.__cgpa = cgpa
    @major.setter
    def major(self, major):
        self.__major = major