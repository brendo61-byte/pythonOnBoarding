"""
What you will learn:
- What is logging
- When to log information
- Machine readable vs human readable

We can create

THIS IS NOT DONE! PLEASE DISREGARD!

"""
import logging

logging.basicConfig(level="DEBUG", filename='program.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


