# Author: Warren Spalding (Shaqiloheal)
# Date: 09/01/2022
# Reads through a file called mbox-short.txt and prints the contents
# of the file (line by line) all in upper case.

fhand = open('mbox-short.txt')

for line in fhand:
    linestrip = line.rstrip()
    print(linestrip)


    


