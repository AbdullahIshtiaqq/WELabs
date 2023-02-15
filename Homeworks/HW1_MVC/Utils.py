def displayHeader():
    print("\n************************************************")
    print("***** Welcome to Student Management System *****")
    print("************************************************")

def displayUserChoices():
    print("1- Faculty")
    print("2- Student")

def displayMainMenu():
    print("\n1- Register")
    print("2- Login")
    print("3- Quit")

def displayLoginMenu():
    print("1- View Profile")
    print("2- Edit Profile")
    print("3- Delete info")

def displayFooter():
    print("\n************************************")
    print("****** Thank you for visiting ******")
    print("************************************")

# checks if password contains small and capital alphabet, digit and special character, if it is so.. returns true otherwise false
def isValidPassword(password):
    small = False
    capital = False
    digit = False
    character = False
    for i in range(len(password)):
        if password[i] >= 'a' and password[i] <= 'z':
            small = True
        elif password[i] >= 'A' and password[i] <= 'Z':
            capital = True
        elif password[i] >= '0' and password[i] <= '9':
            digit = True
        else:
            character = True

    if small and capital and digit and character:
        return True
    else:
        return False

# hides all the characters of password except last two ( for the purpose of printing it on screen )
def getPasswordSecretly(password):
    size = len(password)
    str = password[size-2] + password[size-1]
    starrics = ""
    for i in range(size-2):
        starrics = starrics + "*"
    return (starrics+str)