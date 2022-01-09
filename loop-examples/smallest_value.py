smallest_so_far = -1
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74,15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print('After', smallest_so_far)

# Before -1
# -1 9
# -1 41
# -1 12
# -1 3
# -1 74
# -1 15
# After -1