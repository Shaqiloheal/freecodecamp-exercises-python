while True:
    line = input('> ')
    if line[0] == '#': # print(line) will not output when '#' is entered.
        continue
    if line == 'done': # breaks loop when 'done is entered'
        break
    print(line)
print('Done!')