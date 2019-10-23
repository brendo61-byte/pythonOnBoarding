"""
What you will learn:
- How to add, subtract, multiply divide numbers
- Float division and integer division
- Modulus (finding the remainder)
- Dealing with exponents
- Python will crash on errors (like divide by 0)

Okay now lets do more cool things with variables. Like making python do math for us!

What you need to do:
Pt 1
- solve x = 45 + 4(4/6+2)^5 --- should = 584.391
- solve x = (4/5*5+1)^.5    --- should = 2.23607
Pt 2
- understand why divide0 and divide1 have different results
- what is mod0 and mod1
- write code to determine if 39879827239498734985798 is divisible by 3 without a remainder
Pt 3
- divide a number by 0. Watch what happens. Note the type of error it is
Pt 4
- try to add an int and string together. What happens?
"""

x = 6
y = 2

adder = x + y  # some simple addition
suber = x - y  # some simple subtraction
multr = x * y  # some simple multiplication

divide0 = x / y
divide1 = x // y

mod0 = x % y
mod1 = y % x

power = x ** 6  # the "**" means to the power of

p0 = "Hi "
P1 = " My Name IS"
P2 = " Slime Shady"
P = p0 + P1 + P2
print(P)
