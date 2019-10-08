"""
What you will learn:
- ALL things in python are objects, and objects can be operated on.
- How to get all of keys from a dictionary
- How to get all the values form a dictionary
- How to delete a key/val pair from a dictionary
- How to pop, remove, append, index, get max/min on a list

So we have some basics down dealing with dictionaries and lists but how do we do more useful things with them?

Fist off let's talk about what an object is: an object is a collection of data and methods (we'll go over methods
later but for now think of them like equations (or subroutines from assembly). f(x) = 2x^2 + 1. So we can create a
method that takes in x and will return the value of 2x^2 + 1. In short a method operates on data).

EVERYTHING in python is an object! That is why it is an object orientated language. That means all variables in python
have meta data (info about them) and have functions that can operate on them. In python we wrap all this data and method
stuff into a Class - all a class is is an isolated collection of data and methods (more on this later)(side note: this
is why when you print type(*variable*) it prints <class '*name*'> --- because it is THAT class. So int is class, float,
is a class, dict is class, list is class, etc).

Say we have:
a = 5
b = 6

Both are integers but they are independent. So the object that is repressed by the variable a is 100% isolated from the
object repressed by the variable b. a doesn't care if do something to b and vise versa. Each variable is in its own
box.

Why do we care?

Well because we can do powerful stuff knowing this!

Let's go though the examples...

What you need to do:
Pt 1
- Create a while that counts from 0 to 100. Append each number to a list. It should go [1,2,3,...,99]
- Print the sum of the list
- Print the length of the list
- Print the average value for the list
Pt 2
- Create an empty dictionary (x= {})
- Create a while loop that counts from 0 to 100.
- Append the dictionary such that the key value is the number: number^2
- If the squared number is divisible by 3 and 5 change the value to be "foobarr"
- If the number is divisible by 7 change the value to be "Not you!"
Ex output:
{
    1: 1
    2: 4
    3: 9
    4: 16
    5: 25
    6: 36
    7: "Not you!"
    8: 64
    9: 81
    10: 100
    11: 121
    12: 144
    13: 169
    14: 189
    15: "foobarr"
}
"""
# Example 1
print("Example 1:\n")
x = {"name": "Brendon", "age": 21, "status": "Not dead", "single": True, "Has a car": True}

# Take x, lets say we want to know all the keys in it. How can we do that? Easy:
allKeys = x.keys()
print(x)
print(allKeys)

# Or lets say we need all the values
allVals = x.values()
print(allVals)

# lets say we no longer need the key/val pair "name"
pop = x.pop("name")
print(x)
print(pop)
# Note here that when you pop it returns a value! So you can remove a value same store it like here or just plain remove
# it like this
x.pop("age")
print(x)

# Okay that's cool but what if you don't want to deal with popping and just want delete an entry
del x["single"]
print(x)

# What if we want all the key/value pairs from a dictionary?
items = x.items()
print(items)
# Note here that in this list we have is full of tuples. Tuples are another type of data. There are a pair of values
# separated by a coma - like latitude, longitude.

# Or let's say we need to clear a dictionary? No problem
x.clear()
print(x)

# Example 2
print("Example 2:\n")
x = [0, 1, 2, 3, 4, 5, 6,]
print("Starting X: {}".format(x))
# take our list x. What if we want to add the value 7 to it?
x.append(7)
print("Append 7 to list: {}".format(x))

# now what if we don't like the number 7?
x.remove(7)
print("Remove 7 from list: {}".format(x))

# what if we need to know how many entries are in the list?
test = len(x)
print("Length of the list: {}".format(test))

# what if we need to know the max or min value in the list?
maxim = max(x)
minim = min(x)

print("Max val in list: {}".format(maxim))
print("Min val in list: {}".format(minim))

# how about the sum value of all entries in a list?
sumTotal = sum(x)
print("Sum of all entries in list: {}".format(sumTotal))

# What if we need the value at index 2 of the list
print("Value at index 3: {}".format(x[3]))  # we start counting at 0! so the last index is at len(*list*) - 1

# what if we want the last value?
print("Value at last entry in list: {}".format(x[-1]))
# this of a list like a runners 400 meter track. 0 is the starting point. now if you take 399 steps you are 1 meter from
# the finish line. Or you would go -1 steps and be at the same point. This is the same as in geometry we can go
# - 180 or 180 degrees and be at the same point on a circle.

# What if we want the second to last value?
print("Second to last value in list: {}".format(x[-2]))

# now what if we want to remove the last value in a list and save it?
save = x.pop()
print("pop at index -1: {}".format(save))
print("List after pop: {}".format(x))  # note that this defaults to pop the value at index -1 if we don't specify an index

# so if we want to pop the first entry (index 0) we need to ...
save1 = x.pop(0)
print("pop at index 0: {}".format(save1))
print("List after pop: {}".format(x))
