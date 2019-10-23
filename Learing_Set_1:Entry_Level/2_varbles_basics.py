"""
What you will learn:
- Creation of variables
- Overwriting variables
- printing strings

Now lets go over some basics with variables. What we will create are called global variables. This means ANYWHERE in the
code these variables can be called.

There are several types of variables. We will deal with 3 of the most basic:

int: An integer. EX: 3
float: A floating point number: EX: 3.14159
str: A group of characters: EX: "This is a string" - NOTE the "" marks to denote a string

You can always check the 'type' of variable using the type() call. We'll lean more about this later

What you need to do:
Pt 1
- Understand why the variable x changes after the second print statement
- Create a float variable called y
- print y, change the value of y, then print the new value of why
Pt 2
- print z
- change the value of z
- print the new value of z
Pt 3
- print the type of the newly created z
"""
x = 5

# Print 1
print(x)

x = 12345

# Print 2
print(x)

z = "This is a string"

print(type(x))
