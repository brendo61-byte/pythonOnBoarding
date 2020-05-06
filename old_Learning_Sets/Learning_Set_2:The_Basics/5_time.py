"""
What you will learn:
- Operations on time
- time sense epoch
- datetime objects

In modules 4 we made some fake data and that's cool but it was not really useful. It was a) just random numbers, and b)
had no meta data. We had no idea when those data samples were created! In the last module we saw time.sleep() as a way
of creating a software delay but let's talk more about time.

In python we can deal with time in two main ways: 1) Time sense epoch (00:00:00 UTC on 1 January 1970) in seconds or 2)
as a date-time object. The first is simpler so lets start with that.

Example 1:
It's pretty straight forward. Just a float of how many seconds sense 00:00:00 UTC on 1 January 1970. Note that the
accuracy of this number is based on your CPU. On a Raspberry Pi you can expect 2-3 decimal places of accuracy.

Example 2:
Here we create a DTO of our local time (local), then t1 converts our local time into UTC time. See that t2 and t3 print
the same value as t1.

We can also convert DTO to TSE. Then vise versa TSE to DTO

Example 3:
Okay so now let's create a datetime object with time we pass in. What does this mean? Date time objects just contain
information about time (year, month, day, etc). When we say datetime.datetime.now() those fields of year, month, day, etc
are populated with the values tha match the current time.

These means though we can create our own datetime objects and pass in values.
Note here that we can create datetime objects of type datetime, date, and time.

Example 4:
Let's do some operations on datetime objects. Let's Logan wants to go to dinner (impossible cause that would mean
spending money but maybe he'd do Cane's? ... Do you want Cane's now? Haha fuck you!) reservations at a restaurant at
4:30pm. Then suddenly he realizes that he FORGETS ABOUT A SENIOR DESIGN MEETING! and has to change his reservations to
6pm. How can we do this? Simple.

Or we can compare a two datetime objects. Let's get the today's date and see if it's my birthday!

What you need to do:
At the bottom of this module there is a variable called hw. This is a dict that contains names of students and info
about their homework including the grade they earned ant what time they submitted it. Using this info as in input create
a functions that can:
- Read in the grade of each student. Some students forgot to turn in homework and have None as a grade. This is a 0.
- Check if the student submitted their hw on time. It was due 1 Nov at 6pm. For every hour late dock 5% - students
cannot have negative grades.
- Create a master grade holder that is a dictionary containing all students and their final hw grade. Print this using
the commented out section at the very bottom of this module - change "dict" to the name of your dictionary variable

- NOTE: You should use hw as a global variable

Your output should look like ...
{
    "Amy": {
            "Final Grade": 39
    },
    "Brad": {
            "Final Grade: 0
    }, ...

}

"""
import time
import datetime
import json

# Example 1
print("\n\nExample 1\n")
TSE = time.time()
print("Time Sense Epoch: {}".format(TSE))

x = time.localtime()

# Example 2
print("\n\nExample 2\n")
local = datetime.datetime.now()
t1 = local.utcnow()
t2 = datetime.datetime.now().utcnow()
t3 = datetime.datetime.utcnow()

print(local)
print(t1)
print(t2)
print(t3)

print("Year: {}".format(local.year))
print("Month: {}".format(local.month))
print("Day: {}".format(local.day))
print("Hour: {}".format(local.hour))
print("Min: {}".format(local.minute))
print("Second: {}".format(local.second))

conv = local.timestamp()
print("DTO-to-TSE: {}".format(conv))
otherWay = datetime.datetime.fromtimestamp(time.time())
print("TSE-to-DTO: {}".format(otherWay))

# Example 3
print("\n\nExample 3\n")
dateTime = datetime.datetime(year=1998, month=1, day=23)
justDate = datetime.date(year=1998, month=1, day=23)
print("Custom Date Time Object of my Birthday: {}".format(dateTime))
print(type(dateTime))
print("Custom Date of my Birthday: {}".format(justDate))
print(type(justDate))

justTime = datetime.time(hour=13, minute=30, second=0)
print("Custom Time: {}".format(justTime))
print(type(justTime))

# Example 4
print("\n\nExample 4\n")
first = datetime.time(hour=16, minute=30)
print("First reservation time: {}".format(first))
# change dinner time
second = first.replace(hour=18, minute=0)
print("Second reservation time: {}".format(second))

today = datetime.datetime.now()
brendonBDay = datetime.date(year=1998, month=1, day=23)

if today.month == brendonBDay.month and today.day == brendonBDay.day:
    print("Happy Birthday!")
else:
    if today.month == brendonBDay.month:
        daysToBDay = brendonBDay.day - today.day
        print("Only {} days till your birthday!".format(daysToBDay))
    else:
        nextYearBDay = datetime.date(year=today.year + 1, month=brendonBDay.month, day=brendonBDay.day)
        daysLeft = nextYearBDay - today.date()
        # See here today is a datetime object of type datetime and nextYearBDay is of type date - so we have to convert
        # today into a date object. You can also convert datetime into just time in the same way
        print("There are {} days left till your next birthday!".format(daysLeft.days))

hw = {
    "Amy": {
        "grade": 64,
        "Time": 1572676823.0
    },
    "Brad": {
        "grade": None,
        "Time": 1572677809.0
    },
    "Alex": {
        "grade": 60,
        "Time": 1572590298.0
    },
    "Dillon": {
        "grade": None,
        "Time": 1572591061.0
    },
    "Rhianna": {
        "grade": 89,
        "Time": 1572590301.0
    },
    "Sara": {
        "grade": None,
        "Time": 1572590639.0
    },
    "Jordan": {
        "grade": 97,
        "Time": 1572674570.0
    },
    "Hannah": {
        "grade": None,
        "Time": 1572591401.0
    },
    "Abi": {
        "grade": 68,
        "Time": 1572589751.0
    },
    "Sam": {
        "grade": 72,
        "Time": 1572591009.0
    },
    "Cat": {
        "grade": 85,
        "Time": 1572588399.0
    },
    "Tomas": {
        "grade": None,
        "Time": 1572588220.0
    },
    "Ashly": {
        "grade": None,
        "Time": 1572591074.0
    }
}

# print(json.dumps(dict, indent=4))
