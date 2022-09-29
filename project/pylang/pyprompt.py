import fileinput
import os
import sys
import traceback

# implement a command shell that provides all of the features
# that the course instructor described at the start of lab and are
# further described inside of the README.md file in this repository.

# pwd function
def pwd():
    """Print the current working directory from root all the way up"""
    # set the shell's return code to a zero if able to grab any
    try:
        directory = os.getcwd()
        print(directory)
        # return code 0
        return 0
    except:
        # didn't work, return 1
        return 1


# ls function
