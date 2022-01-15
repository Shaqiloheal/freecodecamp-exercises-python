import os

fname = os.path.join(os.path.dirname(__file__), 'mbox-short.txt')
fhand = open(fname)

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split() # splits whitespace to create list from string
email = words[1] # new variable that selects index 1 from list
print(email)
# stephen.marquard@uct.ac.za (which is index 1 from list)

pieces = email.split('@')
print(pieces)
# ['stephen.marquard', 'uct.ac.za'] - splits two pieces from '@'
print(pieces[1]) # prints index 1 from the list
# uct.ac.za
