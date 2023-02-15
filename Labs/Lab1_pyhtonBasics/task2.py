def print_students(myList):
    for i in range(len(myList)):
        print("Student#",i+1)
        print("Name: ", myList[i]["name"])
        print("Homework Marks: ", myList[i]["hwMarks"])
        print("Quiz Marks: ", myList[i]["quizMarks"])
        print("Project Marks: ", myList[i]["projectMarks"],"\n")

def average(myList):
    sum = 0
    for i in range(len(myList)):
        sum = sum + myList[i]
    total = len(myList)
    average = sum / total
    return average

def get_average_of_students(myList):
    listOfQuiz = []
    for i in range(len(myList)):
        listOfQuiz.append(myList[i]["quizMarks"])
    listOfHw = []
    for i in range(len(myList)):
        listOfHw.append(myList[i]["hwMarks"])
    myTuple = (average(listOfQuiz),average(listOfHw))
    return myTuple

def weighted_average(myTuple,marks):
    weightedAverage = 0.0
    weightedAverage = (marks / 100) * 35
    weightedAverage = weightedAverage + (myTuple[0] / 100) * 40
    weightedAverage = weightedAverage + (myTuple[1] / 100) * 25
    return weightedAverage

def get_letter_grade(marks):
    grade = '\0'
    if(marks >= 80):
        grade = 'A'
    elif(marks >= 70):
        grade = 'B'
    elif(marks >= 60):
        grade = 'C'
    elif(marks >= 50):
        grade = 'D'
    else:
        grade = 'F'
    return grade

def get_class_average(myList):
    listOfWeightedAverages = []
    for i in range(len(myList)):
        myTuple = (myList[i]["quizMarks"],myList[i]["hwMarks"])
        listOfWeightedAverages.append(weighted_average(myTuple,myList[i]["projectMarks"]))

    return average(listOfWeightedAverages)


num = int(input("Enter no of students: "))
listOfDict = []
for i in range(num):
    myDict = {}
    myDict["name"] = input("Enter student name: ")
    myDict["hwMarks"] = int(input("Enter homework marks of student: "))
    myDict["quizMarks"] = int(input("Enter quiz marks  of student: "))
    myDict["projectMarks"] = int(input("Enter project marks of student: "))
    listOfDict.append(myDict)

print_students(listOfDict)

for i in range(num):
    myTuple = (listOfDict[i]["quizMarks"],listOfDict[i]["hwMarks"])
    print("Weighted Average of", listOfDict[i]["name"], ":",weighted_average(myTuple,listOfDict[i]["projectMarks"]))

print("Class Average:", get_class_average(listOfDict))