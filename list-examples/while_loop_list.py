
numlist = list() # creates a list
while True:
    input_num = input('Enter a number: ') # user number input
    if input_num == 'done': # type 'done' to break out of loop.
        break
    value = float(input_num) #converts input into floating point number
    numlist.append(value) # adds number to end of list

average = sum(numlist) / len(numlist) # summates the list then divides the length of list
print('Average:', average)
