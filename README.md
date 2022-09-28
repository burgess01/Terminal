# Command Shell

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/1013818801281839184?logo=discord)](https://discord.gg/9VfCdqffu6)

## Introduction

This project introduces the steps that you must take to implement, build, and
run a Python program called `pyprompt` that provides a simplified command shell
featuring commands such as `cd`, `ls`, `pwd`, and both `quit` and `exit`.
Although this program will not require you to leverage the `fork` and `exec`
system calls provided by your operating system, it will serve as both a vehicle
for exploring the challenges associated with command shell implementation and a
baseline for a more sophisticated implementation of a shell in Python.

## Seeking Assistance

Even though the course instructor will have covered all of the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as you explore the depth and breadth in the field of operating
systems. If you have questions about this project, please schedule a meeting
with the course instructor during office hours.

## Project Overview

After cloning this repository to your computer, please take the following
steps:

### Program Setup

Some of the source code for this project inspired by the content of the [OSTEP
book](http://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf). Please make sure that
you read chapters 5 and 6 and review the slides on the course web site for more
information about these programs! You can also learn more about how a command
shell should behave by using the `bash` or `zsh` command shell on your computer.

### Program Implementation

Your `pyprompt` program should implement the following required commands:

- `pwd` will print the current working directory in a fully qualified fashion,
  ensuring that it displays the root of the file system all the way up to the
  directory from which the command was executed. Unless the `pyprompt` program
  is unable to access the file system to display the name of the current working
  directory, it will always set the shell's return code to a zero value after
  running this command.

- `ls` will print the one or more files and directories that are inside of the
  current working directory. Notably, this command will not recursively display
  the files and directories in all subdirectories of the current directory.
  Instead, it will only display those files and directories that are immediately
  contained by the current working directory. Unless the `pyprompt` program is
  unable to access the file system in the current working directory, it will
  always set the shell's return code to a zero value upon completion of this
  command.

- `cd <directory-name>` will change the shell into the destination directory
  specified by `<directory-name>`. Importantly, the provided `<directory-name>`
  must be relative to the current working directory as reported by the `pwd`
  command. The `cd` command should support the use of `.` and `..` and
  appropriate combinations of those two directory names modifiers. For instance,
  the command `cd .` will keep the shell in the same directory, `cd ..` will
  move the shell one directory back up the file system tree, and `cd ../../`
  will move the shell back up the file system two directory levels. If the `cd`
  command is given an invalid directory, then it will not change to it and it
  will set the `pyprompt` exit code to a non-zero value; otherwise, this command
  will set the return code to a zero value to indicate that it was a success.

- Either the `quit` or the `exit` command will leave the `pyprompt` shell. This
  command will use an `exit` function provided by the Python programming
  language to signal to the operating system as to whether the command shell
  exited with either a zero (i.e., the most recent command did not produce an
  error) or a non-zero exit code (i.e., the most recent command did cause an
  error). Importantly, it is possible for the `pyprompt` shell to return a zero
  exit code &mdash; even if one command in its interaction sequence returned a
  non-zero exit code &mdash; as long as the last command before an `exit` or a
  `quit` worked correctly.

The `pyprompt` program should work in both an interactive and a non-interactive
(i.e., batch) fashion. In its interactive mode, `pyprompt` should accept
commands from an person who is typing at the keyboard. After display the command
shell prompt of `>` the program should accept an input from the user, analyze
the command, and then take the requested action on behalf of the individual.
When `pyprompt` runs in non-interactive mode, it should accept commands through
standard input redirection and the use of the `<` operator in the shell. As it
runs in non-interactive mode, `pyprompt` should read in the command, echo the
command after a prompt symbol of `>` and then take the action required by the
prompt. Ultimately, the output that `pyprompt` produces when run in
non-interactive mode should look the same as if a person typed it in the
terminal window.

Although your program should run interactively during the execution of an
arbitrary number of commands that you type on the keyboard, it should also
return a zero exit code for all of the command scripts provided in the
`commands/` directory. This means that your program must produce the correct
number of lines of output and the correct lines of output for the command
sequences given by every file in the `commands/` directory. It is also important
to note that the automated assessment checks for the seven command sequence
files must complete within the timeout specified in the GitHub Actions
configuration file. Finally, `pyprompt` should capture all exceptions thrown by
the Python runtime environment so as to ensure that no Python stack traces are
displayed even when the person using the program inputs a command sequence like
`CTRL-c`.

For your reference, here is the output of the command `python
project/pylang/pyprompt.py < commands/test_three.cmd` when run on the course
instructor's computer. Please bear in mind that your program will produce
slightly different output depending on where you created the main directory that
houses the source code for this project.

```text
pyprompt 0.1.0

> pwd
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution
> ls
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/project
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/config
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/writing
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/.git
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/README.md
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/.gitignore
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/tags
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/.mdlrc
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/commands
/home/gkapfham/working/teaching/github-classroom/os-sketch/operating-systems/solutions/command-shell-solution/.github
> exit
```

### Project Reflection

As you work on this project, you should regularly take time to reflect on the
steps that you are taking and why you are taking them. Each time you run a
program you should think about the inputs, outputs, and behavior of that
program, jotting down notes to help you remember these insights. When you are
writing Python and Go programs, please reserve time to reflect on the features
of the language that you are learning and how the languages are similar to and
different from each other. As you complete this project, make sure that
you reflect on your own strengths and weaknesses and how you can improve in
advance of the next project. Finally, as you implement the `pyprompt` program
you should adopt the viewpoint of the operating system so as to ensure that you
can correctly create a command shell that operates in a fashion similar to the
`zsh` or `bash` shells.

### Automated Assessment

Please review the following notes about the way in which your project will be
automatically assess in GitHub Actions:

- If you have already installed the
  [GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs
  the automated grading checks provided by
  [GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
  repository's base directory, run the automated grading checks by typing
  `gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical writing
  prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code. This means that instead of only
  deleting the `TODO` marker from the code you should delete the `TODO`
  marker and the entire prompt and then add your own comments to demonstrate
  that you understand all of the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
  labels from every line of the `writing/reflection.md` file. This means that
  you should not simply delete the `TODO` marker but instead delete the entire
  prompt so that your reflection is a document that contains polished technical
  writing that is suitable for publication on your professional web site.
