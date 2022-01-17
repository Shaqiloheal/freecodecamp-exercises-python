lst = list()
lst.append(21)
lst.append(183)
print(lst)
# [21, 183]

lst[0] = 23
print(lst)
# [23, 183]

# Dictionaries are like lists except they use keys instead
# of numbers to look up values

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
# {'age': 21, 'course': 182}

ddd['age'] = 23
print(ddd)
# {'age': 23, 'course': 182}