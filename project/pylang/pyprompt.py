import fileinput
import os
import sys
import stat
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
def exit(returnCode):
    """Exit the shell and return the correct exit code; non-zero code will be zero if exit works right"""

    sys.exit(returnCode)


# main function
def main():
    try:
        print("pyprompt 0.1.0\n")

        mode = os.fstat(0).st_mode
        if stat.S_ISREG(mode):
            for line in fileinput.input():
                # use attrs to take input and feed into correct function
                lineArgs = line.split()
                # first line is command
                returnCode = 0
                if lineArgs[0] == "pwd":
                    print(">pwd")
                    returnCode = pwd()
                elif lineArgs[0] == "ls":
                    print(">ls")
                    returnCode = ls()
                elif lineArgs[0] == "cd":
                    print(">cd")
                    returnCode = cd(lineArgs[1])
                elif lineArgs[0] == "exit":
                    print(">exit")
                    exit(returnCode)
                else:
                    print("Command not found")
                    returnCode = 1
                    exit(returnCode)
        else:
            # if in else this means it was ran in the command line
            stillRunning = True
            while stillRunning == True:
                commandInput = input(">")
                if commandInput == "pwd":
                    returnCode = pwd()
                elif commandInput == "ls":
                    returnCode = ls()
                elif "cd " in commandInput:
                    command, pathName = commandInput.split()
                    returnCode = cd(pathName)
                elif commandInput == "exit":
                    exit(returnCode)
                else:
                    print("Command not found")
                    returnCode = 1
    except KeyboardInterrupt:
        # make sure a Keyboard Interrupt does not crash code
        traceback.print_exc()
        returnCode = 1
        exit(returnCode)


main()
