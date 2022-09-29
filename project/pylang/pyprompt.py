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
def ls():
    """Print the one or more files and directories that are inside of the current working directory"""
    # set the shell's return code to a zero if able to grab any
    try:
        obj = os.scandir(os.getcwd())
        for item in obj:
            if item.is_dir() or item.is_file():
                # if the line is really what we are looking for
                # print out on the terminal
                print(os.getcwd() + "/" + item.name)
        return 0
    except:
        # return failing return code
        return 1


# cd function
def cd(navigation):
    """Move the directory; support . and .."""
    try:
        origDir = os.getcwd()
        os.chdir(navigation)
        return 0
    except:
        # if the directory is not real
        print(navigation, " is not valid")
        # return failing return code
        return 1


# exit function
