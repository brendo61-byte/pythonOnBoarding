import random

NAMES = ["Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin", "Charlotte", "Elijah", "Mia", "Lucas", "Amelia", "Mason",
         "Harper", "Logan", "Evelyn"]


def getAverage(data):
    return sum(data) / len(data)


def getName():
    n = random.randint(0, len(NAMES) - 1)
    name = NAMES.pop(n)

    return name


def getGrades():
    tempGradeList = []
    for i in range(5):
        tempGradeList.append(random.randint(65, 92))

    return tempGradeList


def makeInfo(n):
    temp = {}
    for i in range(n):
        name = getName()
        grades = getGrades()

        temp.update({name: grades})

    return temp
