from ATMException import AccountNotFound
from ATMException import InSufficientBalance
from ATMException import InvalidPin

accountNumGenerator = 1
ch = 0
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
        name = input("Enter username: ")
        flag = True
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

        f = open("atmData.txt","a")
        f.write(name+",ATM"+str(accountNumGenerator)+","+str(pin) +",100\n")
        f.close()
        print("Account created successfully! Your account number is ATM"+str(accountNumGenerator)+"\n")
        accountNumGenerator += 1
    elif ch == 2:
        f = open("atmData.txt","r")
        accountDetails = f.readlines()
        accounts = []
        for i in range(len(accountDetails)):
            tokens = accountDetails[i].split(",")
            balance = tokens[3].split("\n")
            accDict = {"username" : tokens[0], "accountNum" : tokens[1], "password" : tokens[2], "balance" : balance[0]}
            accounts.append((accDict))
        f.close()

        accountNum = input("Enter your account number: ")
        index = -1
        for i in range(len(accounts)):
            if accounts[i]["accountNum"] == accountNum:
                index = i;

        execute = True
        try:
            if index == -1:
                raise AccountNotFound("Account doesn't exist")
        except AccountNotFound as e:
            execute = False
            print(str(e))

        loginSuccessful = False
        if execute:
            tries = 3
            while tries > 0 and loginSuccessful == False:
                print("Tries remaining: ",tries)
                password = input("Enter your password: ")
                if password == accounts[index]["password"]:
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
                print("Account Balance: ", accounts[index]["balance"])
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
                    if(amount > int(accounts[index]["balance"])):
                        print("Insufficient Balance")
                    else:
                        insufficientAmount = False

                newBalance = int(accounts[index]["balance"]) - amount
                accounts[index]["balance"] = str(newBalance)
                f = open("atmData.txt","w")
                for i in range (len(accounts)):
                    f.write(accounts[i]["username"]+","+accounts[i]["accountNum"]+","+accounts[i]["password"]+","+accounts[i]["balance"]+"\n")
                f.close()
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
                newBalance = amount + int(accounts[index]["balance"])
                accounts[index]["balance"] = str(newBalance)
                m = open("atmData.txt", "w")
                for i in range(len(accounts)):
                    m.write(
                        accounts[i]["username"] + "," + accounts[i]["accountNum"] + "," + accounts[i]["password"] + ","+accounts[i]["balance"] + "\n")
                m.close()
        else:
            print("Account Access Denied\n")
    elif ch == 3:
        print("Thank you for using ATM Machine\n")
    else:
        if integerInput:
            print("Invalid choice! Please enter a valid menu option\n")