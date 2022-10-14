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
            lineArgs = []
            returnCode = 0
            for line in fileinput.input():
                lineArgs.append(line.strip())
            for line in lineArgs:
                # iterate through each line
                # get command and feed into that function
                if line == "pwd":
                    print(">pwd")
                    returnCode = pwd()
                elif line == "ls":
                    print(">ls")
                    returnCode = ls()
                elif "cd" in line:
                    print(">cd")
                    command, pathName = line.split()
                    returnCode = cd(pathName)
                elif line == "exit":
                    # Assumes file does not require a True/False
                    listLen = len(lineArgs) - 1
                    if lineArgs.index(line) == listLen:
                        # if exit is the last line in the file (no true/false)
                        print(">exit")
                        exit(returnCode)
                        pass
                    # if there is a True/False, don't want to do anything
                elif line == "True":
                    # if True, build should be passing
                    # do nothing, just exit
                    exit(returnCode)
                elif line == "False":
                    # if False, build should be failing
                    # if exit code 1, make exit code 0
                    # if exit code 0, make exit code 1
                    if returnCode == 0:
                        returnCode = 1
                    else:
                        # means code is 1, needs to equal 0
                        returnCode = 0
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
