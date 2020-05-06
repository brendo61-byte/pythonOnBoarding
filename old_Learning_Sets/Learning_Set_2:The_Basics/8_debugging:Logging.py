"""
What you will learn:
- What is logging
- When to log information

Before we had a bunch of exceptions to handle errors in our code. So let's say we have a sensor platform reading in
values and it catches an error - then what? Well the program didn't behave as we expected so that's a problem. So the
best course of action is to then record the error so we can look at it latter. Right now all we do is print statements
but soon we will need to log them in a real deployment situation. This is because we won't be there to read the prints
- but we need to be able to back and check on the program later.

Now I did just lie to you. You don't ONLY use logging for when an error occurs. That is just a use case. You can log
anything you want! Did the program start correctly? Log that. Did the program start and then crash? Log that. Was there
an error? Yea, log that too! Logging is so that you as a software engineer can go back though the log files and determine
exactly what the program was doing.

There are several levels of logging. Each means it is a more serious thing. The levels, in order of severity, are:
debug, for basic info to debug; info, standard operation info you should know; warning, something went wrong but is not
a big deal, like an error being thrown; and critical, shit is hitting the fucking fan!

Where to put logs is to some degree a personal choice. But it is important to realize that good logging can make or break
debugging. When you have 10,000+ lines of code running on several virtual machines and something goes wrong log files
are your friend.

See example 1 for how to use loggers.

What you need to do:
- Rewrite the program from module 8 using logging. Log when are where you think it's important
"""
import logging

# Logging set up. Means that it will log everything at the debug level or higher, to a file called "program.log", each
# time you run the program you will "w"ite a new file, and that the format will be: timeStamp, log-level, log-message
logging.basicConfig(level="DEBUG", filename='program.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example 1
print("\n\nExample 1\n")
logging.debug("This is a debug level log")
logging.info("This is a info level log")
logging.warning("This is a warning level log")
logging.critical("This is a critical level log")
