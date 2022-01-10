# Author: Warren Spalding (Shaqiloheal)
# Date: 09/01/2022
# Reads through a file called mbox-short.txt and prints the contents
# of the file (line by line) all in upper case.

# for VSC ensure to import OS
import os

# Use this to allow the program to open the file on terminal.
fname = os.path.join(os.path.dirname(__file__), 'mbox-short.txt') 
fhand = open(fname)

for line in fhand:
    # strips newlines 
    linestrip = line.rstrip()
    # convert all characters to uppercase
    lineupper = linestrip.upper()
    print(lineupper)