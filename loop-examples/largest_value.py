largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# Before -1
# 9 9
# 41 41
# 41 12
# 41 3
# 74 74 - the_num > largest_so_far
# 74 15
# After 74