smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None: # use is/is not on booleans and None.
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

# Before
# 9 9
# 9 41
# 9 12
# 3 3
# 3 74
# 3 15
# After 3
