found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

# Before False
# False 9
# False 41
# False 12
# True 3
# True 74
# True 15
# After True