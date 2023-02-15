class User:
    def __init__ (self, name, password):
        self.__username = name
        self.__password = password

    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, name):
        username = name
    @password.setter
    def password(self, password):
        self.__password = password