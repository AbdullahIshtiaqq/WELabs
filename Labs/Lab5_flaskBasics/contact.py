class Contact:
    def __init__(self, name = None, mobileno = None, city = None, profession = None):
        self.__name = name
        self.__mobileno = mobileno
        self.__city = city
        self.__profession = profession

    @property
    def name(self):
        return self.__name
    @property
    def mobileno(self):
        return self.__mobileno
    @property
    def city(self):
        return self.__city
    @property
    def profession(self):
        return self.__profession

    @name.setter
    def name(self, name):
        self.__name = name
    @mobileno.setter
    def mobileno(self, mobileno):
        self.__mobileno = mobileno
    @city.setter
    def city(self,city):
        self.__city = city
    @profession.setter
    def profession(self, profession):
        self.__profession = profession