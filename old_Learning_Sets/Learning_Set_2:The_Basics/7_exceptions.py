"""
What your will learn:
- How to write more hardened code
- Dealing with fail cases
- Use of Exceptions

Remember in Learning set 1 when you created a dictionary and then tried to call a key that didn't exist? Python though
a KeyError. Or if you try to divide by 0 you'll get a ZeroDivisionError. Theses errors occur when Python tries to do
something that is outside the bounds of the programming language its self. So what can it do but say "hey here is an
error".

But if we have code running and an error occurs then the program crashes... How can we make sure that errors don't crash
our program? Rather errors can be dealt with.

This is where try/except comes in. See example 1 for the basics. That's it! Now our code can handle errors.

Let's do better. Example one will except ANY error. So let's see what error that is being caught. See example 2. Now we
can know what kind of error is being caught.

Now let's take it up a notch with our spice weasel. Now we can handle errors by type! In each case we can do something
different to handle that error - or if all errors will be handled the same then we can simply use an "except".

The one issue with all this is that not enough information is being given back to use as a programmer about the error.
We want to know more, so let's take a look at example 4. Wow! Okay that prints out A LOT more info... BUT now we know
more about the error! So when it comes time to debug we can check for what's happening. As a programmer information is
power when it comes to debugging

For tips for debug:
- We have already talked about making modular code. SO DO THAT!
- Gather information. Change variables, use the debugger, print to the terminal (next we will learn about logging then
do that too)
- Once you find an error trace it back! If you're creating a function that solves for standard deviation and the answer
is wrong go check all the parts. Did you solve mean correct? Is there an error in your loops and is causing them to
break?
- Remember the little things. GO BACK TO BASICS. Small errors can cause havoc in a program. Chances are there is
something simple and dumb wrong. Go back to basics to find it. If you're doing division are both type int or float? No?
Then go see why you aren't working with ints and floats? Are those values being read in correctly from a dictionary? Yes?
Okay well is something wrong with how the dictionary is made?
- A good programmer is marked by A) how fast they can debug and 2) avoiding the time costing mistakes in the first place

What you need to do:

At the bottom of this module there is a function called "fakeSupervisor". It will simulators talking to physical hardware
and will generate data sets that have 100 samples in them. For some reason though the hardware is acting kinda wonky.
Samples are not correct but we need data - thus it's become a software problem.
- Create a program that calls "fakeSupervisor" once a second
- Fix the data (see below) then using the fixed dataSet create a list of all the "data" keys
- Using numpy find the standard deviation of the above list. Print it to the screen.
Ensure that ...
- Your program should be able handle to handle ALL ERRORS. It should be able able to run forever.
- Ensure that all values under "data" keys are of type int
- If you cannot read a value in a dictionary print the keys available instead - but only non-standard keys -i.e. if you
have entry={"messUp": 5, "timeStamp": *dateTime object*} only print out "messUp"
- If there is an incorrect key but that key still has a type of data (i.e. an int) then correct the key name and use
the data. i.e: {"messup": 5} -> {"data": 5}
- If you have a data sample that has a "data" value but NO "timeStamp" then create a datetime object that is 0.01 seconds
ahead of the previous data sample
- If the data Sample has data and a timestamp but is not in a dictionary form then put those values into a dictionary.
i.e (5, *dateTime object*) -> {"data", 5, "timeStamp": *dateTime object*}
- If it cannot clean up the data Sample discard it

Suggested steps:
1) Read in a data set from fakeSupervisor
2) Create a new empty list (x=[])
3) Loop though all entries in the data set. If necessary clean the data sample up and append data samples to x
4) Create a new empty list (y=[])
5) loop though x and pull out all "data" values
6) pass y to numpy to solve for standard deviation
7) sleep for 1 second then repeat

Tips:
- USE THE DEBUGGER!
- Use exceptions! - But don't overuse. Use them for debug. When you're program is done you should only have one exception.
- Think ahead. If you do a what happens to b-though-zzz
- If you are doing more than 3-5 "things" then make those "things" a new function
- If that "thing(s)" is a big "thing(s)" then like 1-2 big "thing(s)" per function

"""
import traceback as tb  # we can change how we import things using "as" - this can allow shorthand for long import names
import random
import datetime as DT

# Example 1
print("\n\nExample 1\n")
try:
    x = 1 / 0
except:
    print("You tried to divide by 0")

# Example 2
print("\n\nExample 2\n")
try:
    x = 1 / 0
except Exception as e:
    print("Exception: {}".format(e))

someData = [{"data": 1}, {"data": 2}, {"data": 0}, {"messUp": 4}]

# Example 3
print("\n\nExample 3\n")
for dataSample in someData:
    try:
        val = 5 / dataSample["data"]
    except ZeroDivisionError as ZDE:
        print("\ndataSample being operated on: {}".format(dataSample))
        print("You tried to divide by 0\nError: {}".format(ZDE))
    except Exception as e:
        print("\ndataSample being operated on: {}".format(dataSample))
        print("Unknown Error: {}".format(e))

# Example 4
print("\n\nExmaple 4\n")
for dataSample in someData:
    try:
        val = 5 / dataSample["data"]
    except Exception as e:
        print("\ndataSample being operated on: {}".format(dataSample))
        print("Unknown Error: {}\nTraceBack: {}".format(e, tb.format_exc()))


def fakeSupervisor():
    dataSet = []

    while len(dataSet) < 100:
        someInt = random.randint(0, 10)
        dataSet.append(makePackage(someInt))

    return dataSet

def makePackage(data):
    num = random.random()
    nowTime = DT.datetime.utcnow()

    if num < 0.2:
        return None
    elif num < 0.4:
        return {"messUp": data}
    elif num < 0.6:
        return data, nowTime
    elif num < 0.8:
        return {"data": "Wrong!", "timeStamp": DT}
    else:
        return {"data": data, "timeStamp": DT}
