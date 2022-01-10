fname = input('Please enter the file name including the extention: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Please enter the file name including the extention: mbox.txt
# There were 1797 subject lines in mbox.txt

# Please enter the file name including the extention: mbox-short.txt
# There were 27 subject lines in mbox-short.txt