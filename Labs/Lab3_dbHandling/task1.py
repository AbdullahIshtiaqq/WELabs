import pymysql

class InvalidPin(Exception):
    pass

class User:
    def __init__(self,accNum,passw,accBal):
        self.__accountNumber = accNum
        self.__password = passw
        self.__accountBalance = accBal

    @property
    def accountNumber(self):
        return self.__accountNumber
    @property
    def password(self):
        return self.__password
    @property
    def accountBalance(self):
        return self.__accountBalance

    @accountNumber.setter
    def accountNumber(self, accNum):
        self.__accountNumber = accNum
    @password.setter
    def password(self, passw):
        self.__password = passw
    @accountBalance.setter
    def accountBalance(self, accBal):
        self.__accountBalance = accBal

    def displayData(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host="localhost", user="root", password="272hair5602", database="myfirstdb")
            mydbCursor = mydb.cursor()

            sql = "Select account_no,account_balance from users"
            mydbCursor.execute(sql)
            myresults = mydbCursor.fetchall()
            for r in myresults:
                print("Account Number:", r[0], "Account Balance:", r[1])

        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()
            if mydb != None:
                mydb.close()

class ATM(User):
    def __init__(self,accNum,passw,accBal):
        self.__accountNumber = accNum
        self.__password = passw
        self.__accountBalance = accBal
        self.__accountNumGenerator = 1
    def register_account(self):
        pin = input("Enter your pin: ")
        if len(pin) != 4:
            raise InvalidPin("Invalid pin. Please enter 4 digit numeric key")
        for i in range(4):
            if pin[i] < '0' or pin[i] > '9':
                raise InvalidPin("Invalid pin. Please enter 4 digit numeric key")
        self.__password = pin

        self.__accountNumber = "ATM" + str(self.__accountNumGenerator)
        self.__accountBalance = 100
        print("Account created successfully! Your account number is ATM" + str(self.__accountNumGenerator) + "\n")
        self.__accountNumGenerator += 1
    def login(self):
        loginSuccessful = False
        tries = 3
        while tries > 0 and loginSuccessful == False:
            print("Tries remaining: ", tries)
            password = input("Enter your password: ")
            if password == self.__password:
                loginSuccessful = True
            else:
                print("Wrong Password")
                tries -= 1

        loginCh = 0
        if loginSuccessful:
            print("1-BalanceInquiry\n2-Withdraw\n3-Deposit")
            valid = True
            while valid:
                try:
                    loginCh = int(input("Enter your choice: "))
                    valid = False
                except Exception as e:
                    print("Not an integer, please re-enter your choice")
            while loginCh < 1 or loginCh > 3:
                print("Invalid option, please choose 1-3")
                valid = True
                while valid:
                    try:
                        loginCh = int(input("Enter your choice: "))
                        valid = False
                    except Exception as e:
                        print("Not an integer, please re-enter your choice")
            if loginCh == 1:
                print("Account Balance: ", self.__accountBalance)
            elif loginCh == 2:
                invalidAmount = True
                insufficientAmount = True
                while insufficientAmount:
                    while invalidAmount:
                        try:
                            amount = int(input("Enter amount to withdraw: "))
                            invalidAmount = False
                        except Exception as e:
                            print("Invalid amount entered, please enter a numeric value")
                    while amount < 0:
                        print("Please enter a positive amount to withdraw")
                        invalidAmount = True
                        while invalidAmount:
                            try:
                                amount = int(input("Enter amount to withdraw: "))
                                invalidAmount = False
                            except Exception as e:
                                print("Invalid amount entered, please enter a numeric value")
                    if (amount > self.__accountBalance):
                        print("Insufficient Balance")
                    else:
                        insufficientAmount = False

                self.__accountBalance = self.__accountBalance - amount

            elif loginCh == 3:
                invalidAmount = True
                while invalidAmount:
                    try:
                        amount = int(input("Enter amount to deposit: "))
                        invalidAmount = False
                    except Exception as e:
                        print("Invalid amount entered, please enter a numeric value")
                while amount < 0:
                    print("Please enter a positive amount to deposit")
                    invalidAmount = True
                    while invalidAmount:
                        try:
                            amount = int(input("Enter amount to deposit: "))
                            invalidAmount = False
                        except Exception as e:
                            print("Invalid amount entered, please enter a numeric value")
                self.__accountBalance = amount + self.__1accountBalance
        else:
            print("Account Access Denied\n")

t=ATM("","",0)
try:
    t.register_account()
    t.login()
except InvalidPin as e:
    print(str(e))