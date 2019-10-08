"""
What you will lean:
- Lean about True and False
- How to evaluate a function
- Use mathematical expressions to determine properties of something
- Check types using is

Pt 1:
We can create variables in python that are of type 'bool': True or False --- 1 or 0
This can check conditions. Like "is 5 greater than 3" -> True
Or use as a flag (it's not really a flag but you can think of it similar to flags in Assembly). For Ex: "Is the program
just starting? Yes (i.e True), okay do this first (then set variable to = False).

We can also check the truth of mathematical expressions.
Lets say we have an expression: 34 > 4. Is this correct? Python will evaluate this as either True or False.

Let's say we we have $35. X is how much we have spent. So as long as X<=35 we are good! Python can do
this math too.

Pt 2:
Okay now let's say we are debugging and we are getting something weird. In Module 3 we saw that you cannot add ints and
strings. So maybe we are getting variables that are the wrong type and don't play nice together. We can check check to
see if the types of variables are what we expected!

As we move forward I'll often print out the type of a variable. THIS IS IMPORTANT. To understand python you need to
know what kind of variable you are working with. Later this will become what kind of data object we are working with
and THAT'S when you start getting powerful. BUT it all starts with knowing the base layers.

What you need to do:
- Look at the example at the end of this module. Using that info uncomment the code at the bottom of this module (the
bit that says "Your code here". Remove the ""' marks at the top and bottom). Cast x to be a float and int.
Check to make sure your print statements are correct.
- Just understand the above and what is written below. Module 5 will use this knowledge for some fun stuff.
"""
val0 = 45 < 55
print(val0)

val1 = 456 <= 456
print(val1)

val2 = 44 == 44  # Note that = means equal to and == means check if both sides of the expression are equal
print(val2)

val3 = val2 is bool
print(val3)

x = 34
val4 = x is int
val5 = x is float
print(val4)
print(val5)

# Example
x = 45
print(type(x))
ex = x is str
print(ex)

x = str(x)  # this is called casting. It will try and change the type of a variables to that you are casting it to
# in this case you are changing 34 to "34". You could also do float(x) and be returned 34.0. You can also cast int and
# floats to strings using str()

ex = x is str
print(ex)

"""
# Your code here:
print("Your Code:\n\n"")
x = "45.5"

val0 = x is float
print("Is x a float: {}".format(val0))
val1 = x is int
print("Is x an int: {}".format(val1))
"""
