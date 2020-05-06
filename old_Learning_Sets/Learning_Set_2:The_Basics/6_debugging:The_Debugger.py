"""
What you will learn:
- Code can get complex
- Write code that is easy to debug
- Use the debugger to help find errors

At this point I'm sure you have realized that coding can be hard. Often, something really dumb is what blocks your
program from working. So how can we begin to avoid this? Well the first thing we can do is make code modular. Break a
big task into lots of small steps (i.e. functions). This way if a problem happens we can move though the code one step
at a time and find the bug.

Look at example 1 and example 2. Both sets of code are doing the same: taking in two strings A and B - both only made of
lower case letters, if string B is anywhere in string A then set string found in A to be capital.

Input: A="next level engineers are expected to execute given tasks", B="ex"
Output:  "nEXt level engineers are EXpected to EXecute given tasks"

Assuming you are using PyCharm look in the top right corner of the screen there is a bug looking icon. Click it. This is
the debugger. You can execute code in the debugger to help you solve problems. To go to a line of code break points can
be added - simply click to the right of the line number and a red dot will appear. The debugger will run code until the
break point and then stop. You can then begin to step though code line by line - or run again.

Note that the debugger will display variable names on the screen for you. This is really handy to make sure your logic
is working as expected.


On Coding as a whole ...

There are many ways philosophy when it comes to writing code but here are a few too keep in mind ...
 --- The Zen of Python ---

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


This comes with my own thoughts on the subject and some things you SHOULD keep in mind while working though this
training:

Functionality is paramount
Until your peers have to update it, then readability is key
Reliability should be absolute
Or absolutely accounted for

Write code that works, is clean and easy to read, and can handle errors. The sensors we are building have to run
24/7/365 so your code needs to be hardened so that it NEVER FAILS ... and when it does fail it can do fail
in a controlled manor.

While keeping in mind that there years of teams behind us that will use what we have created. Therefor we must write
programs that are clean and easy to read. You should view the idea of good code the same you view a good essay:
organized, well thought-out, easy to understand what the author is trying to say.

The better you are at organizing code the easier it is to debug.
The better you are at creating well thought-out code the better it will handle the unexpected.
The better you are at writing easy to read code the easier it will be for your peers to use it too.

What you need to do:
- Fix the two programs below using the debugger so that they output the correct values.
- USE THE DEBUGGER
- You can change whatever you want inside each function BUT 'stringChanger' must use a while loop and 'stringAlter' must
use a for loop.
- Which function was easier to debug? Why?
"""
# Example 1
print("\n\nExample 1\n")


def stringChanger(A, B):
    temp = ""
    count = 0

    while count < len(A) - 1:
        charToCheck = A[count]
        if charToCheck == "e":
            temp += charToCheck.upper()
            nextCharToCheck = A[count + 1]
            if nextCharToCheck == "x":
                temp += nextCharToCheck.upper()
                count += 1
        else:
            temp += charToCheck

        count += 1

    print(temp)


def stringAlter(A, B):
    temp = ""
    for i in range(0, len(A) - len(B), 1):
        checkStr = A[i:i+len(B)]
        if checkStr == B:
            temp += checkStr.upper()
        else:
            temp += checkStr

    print(temp)


stringAlter(A="next level engineers are expected to execute given tasks", B="ex")
stringChanger(A="next level engineers are expected to execute given tasks", B="ex")
