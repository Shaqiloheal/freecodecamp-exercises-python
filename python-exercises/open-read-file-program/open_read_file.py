# Author: Warren Spalding (Shaqiloheal)
# Date: 09/01/2022
# Reads through a file called mbox-short.txt and prints the contents
# of the file (line by line) all in upper case.
import os

fname = os.path.join(os.path.dirname(__file__), 'mbox-short.txt')
fhand = open(fname)

for line in fhand:
    linestrip = line.rstrip()
    lineupper = linestrip.upper()
    print(lineupper)