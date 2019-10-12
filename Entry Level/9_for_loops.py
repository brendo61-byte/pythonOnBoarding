"""
What you will lean:
- what is a for loop
- how to iterate though lists using for loops

Okay so we went over while loops. They work by doing stuff until the "while" condition is no longer True
Now we have for loops. Let's your mom gives you a list of chorus to do. You have to finish them you don't get any cookies
at dinner. So for a task on the to-do-list we have to do a thing. This is how for-loops work.

Why do we care if we can use while loops? See example the examples ...

What you need to do:
- Complete the problem at the end of this module
"""
import time
import random

# Example 1
print("Example 1:\n")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
while count <= len(x) - 1:
    print(x[count])
    count += 1

# Can we do this better? YES!!!!

for value in x:
    print(value)

# See how we did in with out a count variable, without a mathematical expression, without having to deal with
# length and index numbers, and without increasing the value of our counter. All of this makes the code simpler and cleaner.
# THIS IS IMPORTANT in a team setting. You are not just writing code for yourself. It's for the ENTIRE TEAM! So don't leave
# your teammates shitty code to read though. Make it clear what you are trying to do - if this is starting to sound like
# writing a good paper it's because it should!

# Example 2
print("Example 2:\n")
w = {"name": "Brendon", "age": 21, "major": "EE", "Is Alive?": True}

# Now lets say we have the above dict. We want to print out all the values. How can we do this?

for entry in w.keys():
    val = w[entry]
    print("Key: {} -- Val: {}".format(entry, val))

# Example 3
print("Example 3:\n")
# we can also use for loops to cleanly remove values from lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = a  # we have to use a temp value because we cannot change the length of a list as we iterate over it
for val in temp:
    if val % 2 == 0:
        a.remove(val)

print("List without multiples of 2: {}".format(a))

"""
Okay so let's pull modules 1-9 together. Why do we care? Let's say we have a bunch of data packets from a temperature
sensor (see below). We need to see if the temperature is a safe range and get some basic statistics.
Here we'll introduce timestamps. There are several ways to express time but a common one is time since epoch -i.e. the
number of seconds that have passed sense January 1, 1970, 00:00:00 at UTC (this is when the UNIX OS
launched this time was needed to coordinate things between all systems to a uniform time standard and is still VERY
widely used today).

LAST PROBLEM OF THE ENTRY LEVEL PYTHON ON_BOARDING
_______________________________________________________________________________________________________________________

Data samples for the temperature are collected one a day for 100 days. Each sample is tagged with a timestamp and
a temperature value.

These data samples are stored in the below variable "data".

Using loops, and if statements, and everything else from modules 1-9 write a program that reads in each each data-
sample and does the following:
- Somewhere between days 24 - 67 (inclusively) there was an error reading the temperature. The sensor reported a value
far too hot to be possible. Find this value and remove it from the list.
- We need to know how many days the temperature was over 40. Print this to the screen (omitting the bad data point).
- What is the the average temperature over the 99 days (omitting the bad).
"""

data = [{'Time Stamp': 1570648123.120855, 'Temp': 20}, {'Time Stamp': 1570734523.120863, 'Temp': 47},
        {'Time Stamp': 1570820923.120866, 'Temp': 43}, {'Time Stamp': 1570907323.1208682, 'Temp': 39},
        {'Time Stamp': 1570993723.1208708, 'Temp': 45}, {'Time Stamp': 1571080123.120873, 'Temp': 11},
        {'Time Stamp': 1571166523.1208751, 'Temp': 17}, {'Time Stamp': 1571252923.120877, 'Temp': 2},
        {'Time Stamp': 1571339323.1208792, 'Temp': 49}, {'Time Stamp': 1571425723.1208808, 'Temp': 16},
        {'Time Stamp': 1571512123.120883, 'Temp': 27}, {'Time Stamp': 1571598523.120885, 'Temp': 43},
        {'Time Stamp': 1571684923.120887, 'Temp': 44}, {'Time Stamp': 1571771323.1208892, 'Temp': 9},
        {'Time Stamp': 1571857723.1208909, 'Temp': 1}, {'Time Stamp': 1571944123.120893, 'Temp': 38},
        {'Time Stamp': 1572030523.120895, 'Temp': 57}, {'Time Stamp': 1572116923.120897, 'Temp': 5},
        {'Time Stamp': 1572203323.120899, 'Temp': 22}, {'Time Stamp': 1572289723.120901, 'Temp': 9},
        {'Time Stamp': 1572376123.120903, 'Temp': 9}, {'Time Stamp': 1572462523.120905, 'Temp': 11},
        {'Time Stamp': 1572548923.120907, 'Temp': 9}, {'Time Stamp': 1572635323.120909, 'Temp': 50},
        {'Time Stamp': 1572721723.1209111, 'Temp': 35}, {'Time Stamp': 1572808123.1209128, 'Temp': 49},
        {'Time Stamp': 1572894523.120917, 'Temp': 27}, {'Time Stamp': 1572980923.120919, 'Temp': 58},
        {'Time Stamp': 1573067323.1209211, 'Temp': 9}, {'Time Stamp': 1573153723.120925, 'Temp': 35},
        {'Time Stamp': 1573240123.1209269, 'Temp': 7}, {'Time Stamp': 1573326523.120928, 'Temp': 43},
        {'Time Stamp': 1573412923.12093, 'Temp': 37}, {'Time Stamp': 1573499323.120932, 'Temp': 33},
        {'Time Stamp': 1573585723.1209338, 'Temp': 47}, {'Time Stamp': 1573672123.120936, 'Temp': 11},
        {'Time Stamp': 1573758523.120938, 'Temp': 39}, {'Time Stamp': 1573844923.12094, 'Temp': 17},
        {'Time Stamp': 1573931323.120942, 'Temp': 333}, {'Time Stamp': 1574017723.120944, 'Temp': 37},
        {'Time Stamp': 1574104123.120946, 'Temp': 39}, {'Time Stamp': 1574190523.120948, 'Temp': 48},
        {'Time Stamp': 1574276923.12095, 'Temp': 58}, {'Time Stamp': 1574363323.1209521, 'Temp': 0},
        {'Time Stamp': 1574449723.120954, 'Temp': 29}, {'Time Stamp': 1574536123.120956, 'Temp': 26},
        {'Time Stamp': 1574622523.1209579, 'Temp': 8}, {'Time Stamp': 1574708923.12096, 'Temp': 16},
        {'Time Stamp': 1574795323.1209621, 'Temp': 8}, {'Time Stamp': 1574881723.120965, 'Temp': 49},
        {'Time Stamp': 1574968123.1209679, 'Temp': 17}, {'Time Stamp': 1575054523.12097, 'Temp': 22},
        {'Time Stamp': 1575140923.120973, 'Temp': 0}, {'Time Stamp': 1575227323.120975, 'Temp': 29},
        {'Time Stamp': 1575313723.120977, 'Temp': 14}, {'Time Stamp': 1575400123.1209788, 'Temp': 17},
        {'Time Stamp': 1575486523.120981, 'Temp': 45}, {'Time Stamp': 1575572923.1209831, 'Temp': 55},
        {'Time Stamp': 1575659323.120985, 'Temp': 3}, {'Time Stamp': 1575745723.120987, 'Temp': 26},
        {'Time Stamp': 1575832123.1209888, 'Temp': 25}, {'Time Stamp': 1575918523.120991, 'Temp': 3},
        {'Time Stamp': 1576004923.1209931, 'Temp': 44}, {'Time Stamp': 1576091323.120995, 'Temp': 10},
        {'Time Stamp': 1576177723.1209972, 'Temp': 49}, {'Time Stamp': 1576264123.120998, 'Temp': 46},
        {'Time Stamp': 1576350523.121, 'Temp': 3}, {'Time Stamp': 1576436923.121002, 'Temp': 19},
        {'Time Stamp': 1576523323.121004, 'Temp': 26}, {'Time Stamp': 1576609723.121006, 'Temp': 6},
        {'Time Stamp': 1576696123.1210082, 'Temp': 23}, {'Time Stamp': 1576782523.1210098, 'Temp': 8},
        {'Time Stamp': 1576868923.121012, 'Temp': 20}, {'Time Stamp': 1576955323.121015, 'Temp': 10},
        {'Time Stamp': 1577041723.121017, 'Temp': 36}, {'Time Stamp': 1577128123.121021, 'Temp': 58},
        {'Time Stamp': 1577214523.121023, 'Temp': 15}, {'Time Stamp': 1577300923.121025, 'Temp': 59},
        {'Time Stamp': 1577387323.121026, 'Temp': 8}, {'Time Stamp': 1577473723.1210282, 'Temp': 13},
        {'Time Stamp': 1577560123.1210299, 'Temp': 11}, {'Time Stamp': 1577646523.121032, 'Temp': 14},
        {'Time Stamp': 1577732923.121034, 'Temp': 14}, {'Time Stamp': 1577819323.121036, 'Temp': 34},
        {'Time Stamp': 1577905723.1210382, 'Temp': 35}, {'Time Stamp': 1577992123.1210399, 'Temp': 34},
        {'Time Stamp': 1578078523.121042, 'Temp': 30}, {'Time Stamp': 1578164923.121044, 'Temp': 23},
        {'Time Stamp': 1578251323.121046, 'Temp': 5}, {'Time Stamp': 1578337723.121048, 'Temp': 13},
        {'Time Stamp': 1578424123.1210501, 'Temp': 49}, {'Time Stamp': 1578510523.1210518, 'Temp': 36},
        {'Time Stamp': 1578596923.121054, 'Temp': 38}, {'Time Stamp': 1578683323.121056, 'Temp': 17},
        {'Time Stamp': 1578769723.121058, 'Temp': 37}, {'Time Stamp': 1578856123.1210601, 'Temp': 23},
        {'Time Stamp': 1578942523.1210618, 'Temp': 54}, {'Time Stamp': 1579028923.121063, 'Temp': 13},
        {'Time Stamp': 1579115323.121068, 'Temp': 36}, {'Time Stamp': 1579201723.121071, 'Temp': 17}]
