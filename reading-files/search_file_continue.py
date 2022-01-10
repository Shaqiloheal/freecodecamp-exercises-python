fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # strips newline
    if not line.startswith('From:'): #skips a line using the continue statement
        continue
    print(line)