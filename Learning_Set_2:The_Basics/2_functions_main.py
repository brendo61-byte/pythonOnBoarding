"""
Okay this doesn't count as a module but it needs to be done.

So far we have used python like Matlab or assembly - the program is read from top to bottom. That's not how we really do
it.

line 21 "if__name__== '__main__'" is python magic for "HEY! START RUNNING CODE FROM HERE!"

This allows us to create a main function that will then launch the rest of the program... we will soon reach the point
where programs are made entirely of functions - and soon after functions and classes. Also note that functions can call
other functions!


It is now expected that all programs you write for "What you needs to do" will be started in the same was as bellow.

Examples in modules may or may not be written with the name == main
"""


def starter():
    print("Now the program is now here.")
    thing()
    stuff()


def thing():
    print("Hey now we are here")
    stuff()


def stuff():
    print("Last call!")


if __name__ == '__main__':
    starter()
