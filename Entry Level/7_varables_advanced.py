"""
What you will learn:
- Lists
- Dictionaries
- Lists of dictionaries
- Dictionaries of lists
- Dictionaries of Dictionaries
- Lists of lists

Pt 1
Let's say you are a professor and you need to keep track of all your students by classes. How can we do this? We can
create dictionaries! Think about a physical dictionary in the library. You look up a word and it has a definition. We
call this a key:value pair. Look up the key and it gives you some value.

Example 1 shows the basic structure of dictionaries
Example 2 shows how we can call keys in a dictionary to get a value
Example 3 shows how we can append a key/val pair

Pt 2
Okay let's move on to lists. Lists are, as the name suggests, just a list of stuff! Like like any old to-do list you
write for school, work, or what you need to get at the grocery store.

Example 4 shows the basic structures of lists
Example 5 shows how put lists inside of lists
Example 6 shows how we can put lists inside a dictionary

What you need to do:
- Create a dictionary called testDict with a key called "TEST" and value of "DONE". Print the value at key "TEST" -
print(testDict["TEST]). Then try to print another key's value print(testDict["OTHER"]). What happens?
- Take the value of x in Example 6, and a under the student Nolan add a list of classes (just make up some random
class numbers) so that it looks like the student Brendon.
"""
# Example 1. Not how we can use strings or ints as both keys and values
print("Example 1:\n")
w = {"name": "Brendon"}
x = {"ID": 1}
y = {3: "This is a three"}
z = {3: 9}
print("{}\n{}\n{}\n{}\n".format(w, x, y, z))  # we an print values using the '{}' and then following the string with
# .format(). Note that the order in format is important as it will correspond with the position the variables are put in
# the string

# Example 2
print("Example 2:\n")
# For this example we will create a dictionary of dictionaries (or nested dictionary)
x = {
    "students": {
        "Brendon": {
            "Major": "Electrical Engineering",
            "Year": "Senior"
        },
        "Nolan": {
            "Major": "Mechanical Engineering",
            "Year": "Graduated"
        }
    }
}

print(x)
x0 = x["students"]
print(x0)
print(type(x0))

x1 = x["students"]["Nolan"]
print(x1)
print(type(x1))

x2 = x["students"]["Nolan"]["Year"]
print(x2)
print(type(x2))
# See here we can call a key "students" and we will be returned a a dictionary.
# The only value that is not a dictionary is at the bottom layer. x["students"]["Nolan"]["Year"] is of type string


# Example 3
print("Example 3:\n")
# Now let's say we want to add something to a dictionary. Let's say update your info on Facebook
y = {"Address": "1234 North Dr, Fort Collins CO", "age": 21, "Friends": 351}
print(y)
# Lets say you want to include your relationship status:
y["Relationship"] = "It's complicated"
print(y)
# Or lets say you move and need to change your address
y["Address"] = "333 Circle Road, Loveland CO"

# Example 4
print("Example 4\n")
x = [1, 2, 3, 4, 5]
y = ["Square", "Triangle", "Circle"]
print(x)
print(type(x))
print(y)
print(type(y))

# Example 5
print("Example 5:\n")
x = [[1, 2, 3], ["Batman", "Superman", "Pizza Delivery Person"], [{3: 9}, {"age": 21}, {"name": "Brendon"}]]
# Now this may not seem super useful but notice how every nested list contains its own type of information: ints,
# str, and dicts... we can use lists of lists to separate data
# NOTE: We have a list of dictionaries... We'll come back to that in module 9 but it is important!
print(x)

# Example 6
print("Example 6:\n")
# Lets go back to example 2 where we had nested dictionaries with information about students
"""
x = {
    "students": {
        "Brendon": {
            "Major": "Electrical Engineering",
            "Year": "Senior"
        },
        "Nolan": {
            "Major": "Mechanical Engineering",
            "Year": "Graduated"
        }
    }
}
"""
# Now lets say we wanted to include classes under each student. We could created a key called values under each student
# and then have a value of a list containing the classes the studnet is taking.
x = {
    "students": {
        "Brendon": {
            "Major": "Electrical Engineering",
            "Year": "Senior",
            "Classes": ["ECE 251", "ECE 451", "ECE 450", "ECE 455", "ECE 401"]
        },
        "Nolan": {
            "Major": "Mechanical Engineering",
            "Year": "Graduated",
        }
    }
}
print(x)
