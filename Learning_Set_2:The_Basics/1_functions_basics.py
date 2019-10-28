"""
What you will learn:
- What a function is
- When to use a function
- How to pass parameters into a function
- Getting values back from a function

At the end of learning set 1 you you created a program that had to do some simple data analysis based on a list of
readings from a sensors. So what happens when we have several sensors and each pushes a list of data like before every
few seconds? How can we handle that? This learning set will get us there.

--- --- ---

But first what is a function? Put simply, it takes inputs, operates on them, and then returns information, or maybe it
doesn't return any information! Functions are kinda like subroutines from 251 but better in every possible way.

Example 1 is the "hello world" of functions - literally.

See example 2. It takes in a value a and b and finds the mid point between them and return this value. Okay, neat but
how can we use that code?

First let's talk about how not to use it. Note that when we print center we don't actually find the mid-point - rather
center is equal to the memory location where the function lives. This might not be super useful right now but it will be
later if you need to pass a function as an argument!

Okay now that's out of the way let's actually find a mid point. See that real calls findMidPoint and passes two variables
that will be used to find the mid point. Also note that real2 does the same thing but is sets the value of each parameter.

One other important thing is that variables created in function are not shared to the outside world. This means the varable
"mid" is unknown outside of the function "findMidPoint".

Let's look into why this is important in example 3. Notice that the position of the input arguments matters!

What you need to do:
- create a function that takes in a,b,c and preforms the quadratic equation solving for x. Return a tuple (assume real
answers)
- create a function that takes in the commented out list called "grades" and using a for loop finds what student has
the highest grade
"""
# Example 1
print("\n\nExample 1\n")

def helloWorld():
    print("Hello World")

helloWorld()

# Example 2
print("\n\nExample 2\n")


def findMidPoint(a, b):
    mid = (a + b) / 2
    return mid


center = findMidPoint
print("\nFunction findMidPoint: {}".format(center))

real = findMidPoint(1, 5)
print("\nReal Function 1: {}".format(real))

real2 = findMidPoint(a=1, b=5)
print("\nReal Function 2: {}".format(real2))

# Example 3
print("\n\nExample 3\n\n")


def foobar(a, b):
    return {"a": a, "b": b}


a = 5
b = 6

t0 = foobar(a, b)
t1 = foobar(b, a)
t2 = foobar(a=a, b=b)

print("a={}\nb={}".format(a, b))
print("t0: {}\nt1: {}\nt2: {}".format(t0, t1, t2))

grades = {"Logan": 92, "Wes": 4, "Brendon": 84, "Abdula": 87, "Tanner": 110, "Tomas": -5}
