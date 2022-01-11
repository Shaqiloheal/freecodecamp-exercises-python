# type 'done' to break out of loop.
numlist = list()
while True:
    input_num = input('Enter a number: ')
    if input_num == 'done':
        break
    value = float(input_num)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
5