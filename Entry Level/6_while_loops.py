"""
What you will lean:
- What is a while loop
- How to write a while
- starting conditions for while loops
- Exit conditions for while loops
- Basics of reusing code

Okay so now we know if a "thing" is True of False. Now let's use that tool for something more powerful: loops.
We will first do "while loops".

Pretend you are drunk and on a mary-go-round:
    You friend bet that you cannot stay on for 10 loops on the mary-go-round. So of course you say you can. You get on
    and they start pushing you in circles. Now each you complete a rotation you count 1 closer to 10. Once you get to
    10 you get off - and promptly puke. BUT THIS IS A FOR LOOP! while count < 10 go spin more then increase count.

    Note how in example 1 we create a starting condition (1)and an ending condition (10). Then we increase the value of
    out variable by 1 each time. IF WE DIDN't WE BE IN A INFINITE LOOP! As long as the expression i < 10 evaluates to
    True we keep running the loop.

    If we run Example 1 how what is the largest number printed? ... Think about why this is the case

What you need to do:
Pt 1
- Create a while loop that prints 0,2,4,6,8,10
- Create a while loop that prints 10,7,4,1
Pt 2
In Example 3 ...
- Change the value of run to True
- inside the while loop create an if statement that checks if k is the 4th multiple of 15. If this is True set run to
False
Pt 3
Challenge Problem (reuse your code form module 5!):
Create a program that can ...
- Create a while loop that counts from 0 to 100.
- If the number count is divisible by only 3 print "foo"
- If the number count is divisible by only 5 print "bar"
- If the number count is divisible by both 5 and 3 print foobarr
- If the number count is not divisible by either 3 or 5 print the number

The first several rows of output should look like this:
1
2
foo
4
bar
foo
7
8
foo
9
bar
11
foo
13
14
foobar
"""
# EX 1
i = 1  # starting condition

while i < 10:
    print(i)
    i += 1  # this is the same as i = 1 + 1

# Ex 2
t = 10
while t > 0:
    print(t)
    t -= 1  # this is the same as t = t - 1

# Ex 3
run = False
k = 1

while run:
    print(k)
    k += 1
