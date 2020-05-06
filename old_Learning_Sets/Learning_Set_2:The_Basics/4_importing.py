"""
what you will learn:
- NEVER rewrite free code
- Chances are someone else has already writen code you need
- how to import external python files and call functions on them

Okay so far you/I have written every line of code in these training sets. That's cool but the power of python comes from
the community and library support behind it. In the Totality software sweet there are ~10,000 lines of code. That's a lot
BUT it imports probably 10-30 times times that and uses those external files to get a lot of the heavy lifting done.

How does a device know what an http packet is and route it to a server? There is a library for that.
How does python talk to databases? Though a library.
How do you create a machine learning algorithm that can identify objects in an image? Yep, by using a library.

Python has built in libraries but there are many more available. If you are a normal person and are using PyCharm then
let's get one other library. In the top menu go:
- PyCharm
- preferences
- project *name of project*
- project interpreter
- click the plus sign at the bottom of the box
- search "numpy"
- its the top one, click on it
- install package

Below we create a program that randomly generates 100 int values between 0 and 9, and then finds the standard deviation
of that data set.

Note that for random we say "random.

What you need to do:
- Just look at this and understand it --- we'll add stuff to it over the next few modules
"""
import random
import numpy
import time

COUNT = 5
DATA_SET_LENGTH = 100


def starter():
    operational = True
    c = 0
    while operational:
        data = getData(DATA_SET_LENGTH)
        std = getSTD(data)

        print("Standard Deviation: {:0.3f}".format(std))  # the ":0.3f" will round a float to 3 decimal places

        c += 1
        if c >= COUNT:
            operational = False
        else:
            time.sleep(.75)  # seconds it will sleep


def getData(length):
    data = []
    start = 0
    while start < length:
        num = random.randint(1, 10)  # generates a random int between 1 and 49 (50 in exclusive)
        data.append(num)
        start += 1
    return data


def getSTD(data):
    std = numpy.std(data)
    return std


if __name__ == '__main__':
    starter()
