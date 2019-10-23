"""
What you will learn:
- What is an if statement
- How does this relate to boolean logic
- Using if to check conditions
- dealing with else
- dealing with ifelse


Okay, let's say your mom said "If you clean your room you can have a cookie" what is going on here. You have been given
a statement: is room clean? Now if the room is clean (if the statement is True) then you get a cookie. If the room is
not clean (the statement is False) then you don't get shit!

If statements in python are the same way. You have a statement. Python checks if it evaluates to True or False. If it is
true then the lines under the if statement are executed. NOTE the indentation. -> See example 1

Lets say you need to check lots of conditions. For example: if you are a boy, if you are over 21, if you like beer.
We can have stacks of if statements. Note: we can check the value of strings! -> see example 2

If/else:

But what if we want to deal with statements that don't evaluate to True. We can use 'else'. -> see example 3

AND/OR/NOT logic:
But what if we need to check multiple conditions? Like if someone is 21 AND likes beer. If this case both statements must
evaluates to True or the if statement is not passed... -> see example 4

We can also do the same thing with nested if statements... -> example 4.1

We can also do 'or' logic. Where if ANY of the presented conditions are True the the statement evaluates to True...
-> see example 5

We can also do inverse logic byt not'ing a boolean. So: not True = False, not False = True ... -> see example 6

If/elif/else:

last thing: Let's say we need to check several conditions but we need to exit on the first true one. For example in a
coil slot coins are often sorted by size. So a dime will fall down the first hole and thus be counted as a dime. A penny
will fall though the second and so forth. But the dime will also fall down the penny hole, or the nickle hole, or the
quarter hole ... so if code how can we ensure that the dime goes though only the correct hole and not the others ...
See example 7

What you need to do:
Write a program that ...:
- take in input x
- checks if x is divisible by 3. Same this as a variable of type bool called q0
- checks if x is divisible by 5. Save this as a variable of type bool called q1
- if x is divisible by 3 and 5 prints "divisible by 3 and 5"
- if x is only divisible by 3 prints "divisible by 3"
- if x is only divisible by 5 print "divisible by 5"
- if x is neither divisible by 5 or 3 then prints the value of x

EX:
Input = 15
Output = "divisible by 3 and 5"

EX:
Input = 9
Output = "divisible by 3"

EX:
Input = 4
Output = 4

"""
if True:
    print("Yes this is True")

# Example 1
print("Example 1:\n")  # The '\n' is a new line character
x = 45

if x > 5:
    print("X is greater than 5")

# Example 2
print("Example 2:\n")
age = 21
boy = True
beer = "yes"

if age >= 21:
    print("Over 21")

if boy:
    print("This dude is a dude my dude")

if beer == "yes":
    print("Yep we like beer!")

# Example 3
print("Example 3:\n")
age = 20
boy = False
beer = "no"

if age >= 21:
    print("Over 21")
else:
    print("Not over 21")

if boy:
    print("This dude is a dude my dude")
else:
    print("This dude is not a dude my dude")

if beer == "yes":
    print("Yep we like beer!")
else:
    print("Na not beer, something stronger!")

# Example 4
print("Example 4:\n")
age = 21
beer = "yes"

if age >= 21 and beer == "yes":  # This will evaluate to True
    print("Cool, lets go get a beer together!")
else:
    print("I cannot get a beer with you")

age = 20
beer = "yes"

if age >= 21 and beer == "yes":  # This will evaluate to False b/c the age check is False
    print("Cool, lets go get a beer together!")
else:
    print("I cannot get a beer with you")

# Example 4.1
print("Example 4.1:\n")
age = 21
beer = "yes"

if age >= 21:  # the second if statement is 'nested' under the first
    if beer == "yes":
        print("Cool, lets go get a beer together!")

# Example 5
print("Example 5:\n")
age = 20
fakeID = True

if age >= 21 or fakeID:
    print("We can get you in the bars")

# Example 6
print("Example 6:\n")
beer = "no"

if not beer == "yes":
    print("Shut up and drink another beer")

# Example 7
print("Example 7:\n")
"""
Okay for this I rated coins based on their size and then ran the code below:
penny = 2
dime = 1
nickle = 3
quarter = 4
silver-dollar = 5

You can change the value of the variable "coin" below. 
"""

coin = 3

if 1 >= coin:
    print("It's a dime")
elif 2 >= coin:
    print("It's a penny")
elif 3 >= coin:
    print("It's a nickle")
elif 4 >= coin:
    print("It's a quarter")
else:
    print("It's a half dollar")
