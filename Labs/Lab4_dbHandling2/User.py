from ATMException import AccountNotFound
from ATMException import InvalidPin
from ATMException import InsufficientBalance
from DBHandler import DBHandler

class User:
    def __init__(self):
        self.__username = None
        self.__password = None

    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password

    @username.getter
    def username(self,name):
        self.__username = name
    @password.getter
    def password(self, passw):
        self.__password = passw

    def register_account(self):
        flag = True
        pin = None
        while flag:
            try:
                pin = input("Enter your pin: ")
                if len(pin) != 4:
                    raise InvalidPin
                for i in range(4):
                    if pin[i] < '0' or pin[i] > '9':
                        raise InvalidPin
                flag = False
            except InvalidPin as e:
                print("Invalid pin. Please enter 4 digit numeric key")

        flag = True
        choice = 0
        while flag:
            try:
                print("Account Types:")
                print("1- Basic Bank Account")
                print("2- Current Account")
                print("3- Savings Account")
                print("4- Fixed Deposit Account")
                choice = int(input("Enter your choice: "))
                if(choice < 1 or choice > 4):
                    raise Exception
                flag = False
            except Exception as e:
                print("Please enter a valid choice")

        mydb = DBHandler("localhost","root","Abcd1234","fcit")
        mydb.register_account(pin,choice)

    def login(self):
        accountNum = input("Enter your account number: ")
        mydb = DBHandler("localhost", "root", "Abcd1234", "fcit")
        mydb.login(accountNum)

ch = 0
user = User()
while ch != 3:
    integerInput = True
    print("1-Register User\n2-Login\n3-Quit")
    try:
        ch = int(input("Enter your choice: "))
    except Exception as e:
        integerInput = False
        ch = 0
        print("Not an integer. Please re-enter your choice\n")

    if ch == 1:
        user.register_account()
    elif ch == 2:
        user.login()
    elif ch == 3:
        print("Thank you for using ATM Machine\n")
    else:
        if integerInput:
            print("Invalid choice! Please enter a valid menu option\n")