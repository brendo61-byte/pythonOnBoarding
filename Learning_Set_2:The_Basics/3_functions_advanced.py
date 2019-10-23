"""
What you will learn:
- When to use a function
- Functions calling functions
- passing dictionaries as arguments

Okay so for this module I'm going to write a program that collects some list of data, does operations on it, and then
prints that information to the screen.

There are limited notes about what is happening to introduce new concepts. Otherwise this is on you to figure out. Use
print statements if need be.

NOTE how larger operations are broken down into smaller chunks. THIS is critical - large code is hard to debug. Modular
code is clear to read though, easier to debug, AND can be ported - i.e. the function below can be copy/pasted into
another program.

What you need to do:
pt 1
- Read though and understand what is happening (being able to read though code is hella important)
pt 2
create function(s) that can be called from "starter" that have the following functionality:
- can be passed a list of data, and an integer value that is an entry in said list (i.e. data and 9 will be passed in)
- determine the percentile of the value - so in the below list 15 is in the 100th percentile and 2 is in the 0th percentile
pt 3
- in starter use a loop to pass this function(s) every entry in the list

"""
x = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4, 15]


# x is global variable. This means it can be accessed everywhere inside this script.


def starter():
    data = getData()
    std = findStandardDeviation(data)

    print("Standard Deviation is: {}".format(std))


def getData():
    return x
    # This is really unnecessary to get x but if you were reading values in from a csv file a function would be nice

def findStandardDeviation(data):
    mean = findMean(data=data)
    # standard deviation = (Sig(x-mean)^2 / n )^0.5, where x=entry, n=length of data, and mean is the, well, mean

    inputs = {"mean": mean, "data": data}
    # above we pass a dictionary as an argument. This will match key names to input parameters.
    variance = sigma(**inputs) / len(data)

    return variance ** 0.5

def sigma(data, mean):
    summation = 0
    for x in data:
        val = x - mean
        squared = val ** 2
        summation += squared

    return summation


def findMean(data):
    sumOfData = sum(data)
    lengthofData = len(data)
    mean = sumOfData / lengthofData
    return mean


if __name__ == '__main__':
    starter()
