from Utils import *
from Controller import *
from Exceptions import *

if __name__ == '__main__':
    displayHeader()
    choice = 0
    while choice != 3:
        # get menu option input ( validates and re-prompt if not valid option chosen )
        try:
            displayMainMenu()
            temp = int(input("Enter your choice: "))
            if temp < 1 or temp > 3:
                raise InvalidChoice("Invalid option entered")
            choice = temp
        except Exception as e:
            print(str(e))

        # if user selects register
        if choice == 1:
            # again get input about which type of user to register and validates it
            userChoice = 0
            displayUserChoices()
            flag = True
            while flag:
                try:
                    userChoice = int(input("Enter user type: "))
                    if userChoice < 1 or userChoice > 2:
                        raise InvalidChoice("Invalid option entered")
                    flag = False
                except Exception as e:
                    print(str(e))

            # gets tha data about the user
            username = input("Enter username: ")
            password = input("Enter password: ")
            while(not isValidPassword(password)):
                print("Your password must contain atleast one lower case alphabet, one upper case alphabet, one digit and one special character")
                password = input("Enter password: ")

            if userChoice == 1:
                # gets faculty specific data
                designation = input("Enter designation: ")
                subject = input("Enter subject in which person holds speciality: ")

                # call to controller
                if register_faculty(username,password,designation,subject):
                    print("Faculty member registered successfully")
                else:
                    print("Can't complete registration")
            else:
                # gets student specific data ( validates for a valid input for both semester and cgpa )
                semester = 0
                flag = True
                while flag:
                    try:
                        semester = int(input("Enter semester: "))
                        if semester < 1 or semester > 8:
                            raise InvalidSemester("Please enter a semester from 1-8")
                        flag = False
                    except Exception as e:
                        print(str(e))

                cgpa = 0.0
                flag = True
                while flag:
                    try:
                        cgpa = float(input("Enter cgpa: "))
                        if cgpa < 0.0 or cgpa > 4.0:
                            raise InvalidCGPA("Please enter cgpa from 0.0-4.0")
                        flag = False
                    except Exception as e:
                        print(str(e))

                major = input("Enter major: ")
                # call to controller
                if register_student(username,password,semester,cgpa,major):
                    print("Student registered successfully")
                else:
                    print("Can't register student")
        # else if user chooses login
        elif choice == 2:
            # get usernama and password and authenticate it
            username = input("Enter username: ")
            password = input("Enter password: ")

            userChoice = 0
            displayUserChoices()
            flag = True
            while flag:
                try:
                    userChoice = int(input("Enter user type: "))
                    if userChoice < 1 or userChoice > 2:
                        raise InvalidChoice("Invalid option entered")
                    flag = False
                except Exception as e:
                    print(str(e))

            if userChoice == 1:
                myTuple = authenticate_faculty(username,password)
                fac_id = myTuple[1]
                # if authentication failed, display error message
                if fac_id == 0:
                    print("Can't log you in. Please recheck your username and password.")
                # otherwise display login menu and ask for choice
                else:
                    faculty = myTuple[0]
                    loginChoice = 0
                    displayLoginMenu()
                    flag = True
                    while flag:
                        try:
                            loginChoice = int(input("Enter your choice: "))
                            if loginChoice < 1 or loginChoice > 3:
                                raise InvalidChoice("Invalid option entered")
                            flag = False
                        except Exception as e:
                            print(str(e))

                    # prints the information of the user
                    if loginChoice == 1:
                        print("\nUsername:",faculty.username)
                        print("Password:",getPasswordSecretly(faculty.password))
                        print("Designation:",faculty.designation)
                        print("Subject:",faculty.subject)
                    # gets new data about user and call to controller to update it
                    elif loginChoice == 2:
                        newDesign = input("Enter new designation (press enter to skip): ")
                        newSubj = input("Enter new subject (press enter to skip):")
                        if newDesign == "":
                            newDesign = faculty.designation
                        if newSubj == "":
                            newSubj = faculty.subject
                        if update_faculty(username,password,newDesign,newSubj):
                            print("Record updated successfully")
                        else:
                            print("Can't update data")
                    # deletes info anout the user
                    else:
                        if delete_faculty(fac_id):
                            print("Faculty member deleted successfully")
                        else:
                            print("Error deleting info")
            else:
                myTuple = authenticate_student(username, password)
                std_id = myTuple[1]
                # if authentication failed, display error message
                if std_id == 0:
                    print("Can't log you in. Please recheck your username and password.")
                # otherwise display login menu
                else:
                    student = myTuple[0]
                    loginChoice = 0
                    displayLoginMenu()
                    flag = True
                    while flag:
                        try:
                            loginChoice = int(input("Enter your choice: "))
                            if loginChoice < 1 or loginChoice > 3:
                                raise InvalidChoice("Invalid option entered")
                            flag = False
                        except Exception as e:
                            print(str(e))

                    # prints the information of the user
                    if loginChoice == 1:
                        print("\nUsername:", student.username)
                        print("Password:", getPasswordSecretly(student.password))
                        print("Semester:", student.semester)
                        print("CGPA:", student.cgpa)
                        print("Major:",student.major)
                    # gets new data about user and call to controller to update it
                    elif loginChoice == 2:
                        newSem = student.semester
                        newCgpa = student.cgpa
                        newMajor = student.major

                        opt = input("Do you want to update semester? (y/n): ")
                        while opt != "Y" and opt != "y" and opt != "n" and opt != "N":
                            opt = input("Please enter either Y (for yes) or N (for No): ")

                        if opt == "y" or opt == "Y":
                            newSem = 0
                            flag = True
                            while flag:
                                try:
                                    newSem = int(input("Enter semester: "))
                                    if newSem < 1 or newSem > 8:
                                        raise InvalidSemester("Please enter a semester from 1-8")
                                    flag = False
                                except Exception as e:
                                    print(str(e))

                        opt = input("Do you want to update CGPA? (y/n): ")
                        while opt != "Y" and opt != "y" and opt != "n" and opt != "N":
                            opt = input("Please enter either Y (for yes) or N (for No): ")

                        newCgpa = 0.0
                        flag = True
                        while flag:
                            try:
                                newCgpa = float(input("Enter cgpa: "))
                                if newCgpa < 0.0 or newCgpa > 4.0:
                                    raise InvalidCGPA("Please enter cgpa from 0.0-4.0")
                                flag = False
                            except Exception as e:
                                print(str(e))

                        newMajor = input("Enter new Major (press enter to skip):")
                        if newMajor == "":
                            newMajor = student.major

                        if update_student(username, password, newSem, newCgpa, newMajor):
                            print("Record updated successfully")
                        else:
                            print("Can't update data")
                    else:
                        # deletes info anout the user
                        if delete_student(std_id):
                            print("Student deleted successfully")
                        else:
                            print("Error deleting info")
        else:
            displayFooter()