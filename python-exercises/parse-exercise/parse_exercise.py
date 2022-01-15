# Author: Warren Spalding (Shaqiloheal)
# Date: 16/01/2022


import os

fname = os.path.join(os.path.dirname(__file__), 'mbox-short.txt') 
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
