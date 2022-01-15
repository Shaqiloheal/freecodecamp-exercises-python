import os

fname = os.path.join(os.path.dirname(__file__), 'mbox-short.txt')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

# Sat
# Fri
# Fri
# Fri
# ...

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)
# ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']