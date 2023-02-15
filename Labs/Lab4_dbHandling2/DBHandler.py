import pymysql
from ATMException import AccountNotFound
from ATMException import TransactionNotAllowed

class DBHandler:
    def __init__(self, host, username, password, db):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__databse = db

    def register_account(self, password, type):
        mydb = None
        cursor = None
        try:
            mydb = pymysql.connect(host = self.__host,  user = self.__username, password = self.__password, database=self.__databse)
            cursor = mydb.cursor()
            query = "select count(*) from users"
            cursor.execute(query)
            accNum = cursor.fetchone()
            query = "insert into users (account_number, password, balance, type, interest_rate, no_of_transactions) values (%s, %s, %s, %s, %s, %s)"

            rate = 0.0
            if type == 3:
                rate = 4
            elif type == 4:
                rate = 8.26
            args = ("ATM" + str(accNum[0]),password,100,type,rate,0)
            cursor.execute(query,args)
            mydb.commit()
            print("Account created succuessfully. Your account number is ATM"+str(accNum[0]))
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()

    def login(self, accNum):
        mydb = None
        cursor = None
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__username, password=self.__password,
                                   database=self.__databse)
            cursor = mydb.cursor()
            query = "select password from users where account_number = %s"
            cursor.execute(query,(accNum))
            passw = cursor.fetchone()
            if passw == None:
                raise AccountNotFound("Account doesn't exist")

            loginSuccessful = False
            tries = 3
            while tries > 0 and loginSuccessful == False:
                print("Tries remaining: ", tries)
                password = input("Enter your password: ")
                if password == passw[0]:
                    loginSuccessful = True
                else:
                    print("Wrong Password")
                    tries -= 1

            loginCh = 0
            if loginSuccessful:
                print("1-BalanceInquiry\n2-Withdraw\n3-Deposit\n4-Transfer")
                valid = True
                while valid:
                    try:
                        loginCh = int(input("Enter your choice: "))
                        valid = False
                    except Exception as e:
                        print("Not an integer, please re-enter your choice")
                while loginCh < 1 or loginCh > 4:
                    print("Invalid option, please choose 1-4")
                    valid = True
                    while valid:
                        try:
                            loginCh = int(input("Enter your choice: "))
                            valid = False
                        except Exception as e:
                            print("Not an integer, please re-enter your choice")
                if loginCh == 1:
                    query = "select balance from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    bal = cursor.fetchone()
                    print("Account Balance: ", bal[0])
                elif loginCh == 2:
                    query = "select type from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    tempType = cursor.fetchone()
                    type = int(tempType[0])

                    addAmount = 0
                    if type == 1:
                        query = "select no_of_transactions from users where account_number = %s"
                        cursor.execute(query, (accNum))
                        tempTransaction = cursor.fetchone()
                        no_of_transaction = int(tempTransaction[0])
                        if no_of_transaction >= 4:
                            addAmount = 100
                    elif type == 4:
                        raise TransactionNotAllowed("Can't perform transaction")

                    query = "select balance from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    bal = cursor.fetchone()
                    invalidAmount = True
                    insufficientAmount = True
                    amount = 0
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
                        if (amount > int(bal[0]) + addAmount):
                            print("Insufficient Balance")
                        else:
                            insufficientAmount = False

                    query = "update users set balance = %s where account_number = %s"
                    newBal = int(bal[0]) - amount - addAmount
                    args = (newBal, accNum)
                    cursor.execute(query,args)
                    mydb.commit()
                    print("Withdrawal successful")
                    query = "select no_of_transactions from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    tempTransaction = cursor.fetchone()
                    no_of_transaction = int(tempTransaction[0])
                    query = "update users set no_of_transactions = %s where account_number = %s"
                    args = (no_of_transaction + 1, accNum)
                    cursor.execute(query, args)
                    mydb.commit()
                elif loginCh == 3:
                    query = "select type from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    tempType = cursor.fetchone()
                    type = int(tempType[0])

                    addAmount = 0
                    if type == 1:
                        query = "select no_of_transactions from users where account_number = %s"
                        cursor.execute(query, (accNum))
                        tempTransaction = cursor.fetchone()
                        no_of_transaction = int(tempTransaction[0])
                        if no_of_transaction >= 4:
                            addAmount = 100
                    elif type == 4:
                        raise TransactionNotAllowed("Can't perform transaction")

                    invalidAmount = True
                    while invalidAmount:
                        try:
                            amount = int(input("Enter amount to deposit: "))
                            invalidAmount = False
                        except Exception as e:
                            print("Invalid amount entered, please enter a numeric value")
                    while amount - addAmount < 0:
                        print("Please enter a positive amount to deposit")
                        invalidAmount = True
                        while invalidAmount:
                            try:
                                amount = int(input("Enter amount to deposit: "))
                                invalidAmount = False
                            except Exception as e:
                                print("Invalid amount entered, please enter a numeric value")

                    query = "select balance from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    bal = cursor.fetchone()

                    query = "update users set balance = %s where account_number = %s"
                    newBal = int(bal[0]) + amount - addAmount
                    args = (newBal, accNum)
                    cursor.execute(query, args)
                    mydb.commit()
                    print("Deposit successful")
                    query = "select no_of_transactions from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    tempTransaction = cursor.fetchone()
                    no_of_transaction = int(tempTransaction[0])
                    query = "update users set no_of_transactions = %s where account_number = %s"
                    args = (no_of_transaction + 1, accNum)
                    cursor.execute(query, args)
                    mydb.commit()
                elif loginCh == 4:
                    self.transfer(accNum)
            else:
                print("Account Access Denied\n")

        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()

    def transfer(self, accNum):
        mydb = None
        cursor = None
        try:
            mydb = pymysql.connect(host=self.__host, user=self.__username, password=self.__password,
                                   database=self.__databse)
            cursor = mydb.cursor()
            query = "select password from users where account_number = %s"
            cursor.execute(query, (accNum))
            passw = cursor.fetchone()
            if passw == None:
                raise AccountNotFound("Account doesn't exist")

            loginSuccessful = True

            if loginSuccessful:
                query = "select type from users where account_number = %s"
                cursor.execute(query, (accNum))
                tempType = cursor.fetchone()
                type = int(tempType[0])

                addAmount = 0
                if type == 1:
                    query = "select no_of_transactions from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    tempTransaction = cursor.fetchone()
                    no_of_transaction = int(tempTransaction[0])
                    if no_of_transaction >= 4:
                        addAmount = 100
                elif type == 4:
                    raise TransactionNotAllowed("Can't perform transaction")

                query = "select balance from users where account_number = %s"
                cursor.execute(query, (accNum))
                bal = cursor.fetchone()
                invalidAmount = True
                insufficientAmount = True
                amount = 0
                while insufficientAmount:
                    while invalidAmount:
                        try:
                            amount = int(input("Enter amount to transfer: "))
                            invalidAmount = False
                        except Exception as e:
                            print("Invalid amount entered, please enter a numeric value")
                    while amount < 0:
                        print("Please enter a positive amount to transfer")
                        invalidAmount = True
                        while invalidAmount:
                            try:
                                amount = int(input("Enter amount to transfer: "))
                                invalidAmount = False
                            except Exception as e:
                                print("Invalid amount entered, please enter a numeric value")
                    if (amount > int(bal[0]) + addAmount):
                        print("Insufficient Balance")
                    else:
                        insufficientAmount = False

                    accountNum = input("Enter account number to transfer: ")
                    query = "select password from users where account_number = %s"
                    cursor.execute(query, (accountNum))
                    passw = cursor.fetchone()
                    if passw == None:
                        raise AccountNotFound("Account doesn't exist")

                    query = "select balance from users where account_number = %s"
                    cursor.execute(query, (accountNum))
                    bal2 = cursor.fetchone()

                    query = "update users set balance = %s where account_number = %s"
                    newBal = int(bal2[0]) + amount
                    args = (newBal, accountNum)
                    cursor.execute(query, args)
                    mydb.commit()

                    query = "update users set balance = %s where account_number = %s"
                    newBal = int(bal[0]) - amount - addAmount
                    args = (newBal, accNum)
                    cursor.execute(query, args)
                    mydb.commit()
                    print("Transfer successful")
                    query = "select no_of_transactions from users where account_number = %s"
                    cursor.execute(query, (accountNum))
                    tempTransaction = cursor.fetchone()
                    no_of_transaction = int(tempTransaction[0])
                    query = "update users set no_of_transactions = %s where account_number = %s"
                    args = (no_of_transaction + 1, accountNum)
                    cursor.execute(query, args)
                    mydb.commit()

                    query = "select no_of_transactions from users where account_number = %s"
                    cursor.execute(query, (accNum))
                    tempTransaction = cursor.fetchone()
                    no_of_transaction = int(tempTransaction[0])
                    query = "update users set no_of_transactions = %s where account_number = %s"
                    args = (no_of_transaction + 1, accNum)
                    cursor.execute(query, args)
                    mydb.commit()
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            if cursor != None:
                cursor.close()