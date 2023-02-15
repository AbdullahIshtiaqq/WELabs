class Time:
    def __init__(self,hrs,min,sec):
        if hrs >= 0:
            self.__hours = hrs % 24
        else:
            self.__hours = 0

        if min >= 0:
            self.__minutes = min % 60
        else:
            self.__minutes = 0

        if sec >= 0:
            self.__seconds = sec % 60
        else:
            self.__seconds = 0

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, hr):
        if hr >= 0:
            self.__hours = hr % 24
    @minutes.setter
    def minutes(self,min):
        if min >=0:
            self.__minutes = min % 60
    @seconds.setter
    def seconds(self,sec):
        if sec >= 0:
            self.__seconds = sec % 60

    def add_time(self,time1,time2):
        t = Time(0,0,0)
        t.hours = ( time1.hours + time2.hours ) % 24
        t.seconds = ( time1.seconds + time2.seconds ) % 60
        tempMin = 0
        if time1.seconds + time2.seconds >= 60:
            tempMin = 1
        t.minutes = ( time1.minutes + time2.minutes + tempMin) % 60
        if time1.minutes + time2.minutes + tempMin >= 60:
            t.hours += 1
        return t

    def display_time24(self):
        print(self.hours,":",self.minutes,":",self.seconds)

    def display_time12(self):
        hrs = self.hours
        if hrs != 12:
            hrs = hrs % 12
        print(hrs,":",self.minutes,":",self.seconds)

    def display_minute(self):
        min = self.hours * 60
        min += self.minutes
        print("Total Minutes:",min)

    def update_time(self, min):
        t = Time(0,0,0)
        t.minutes = min % 60
        t.hours = int(min / 60)

        t = self.add_time(Time(self.hours,self.minutes,self.seconds),t)
        self.hours = t.hours
        self.minutes = t.minutes
        self.seconds = t.seconds



t = Time(15,30,59)
t.display_time12()
t.display_time24()