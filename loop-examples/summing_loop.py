zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Before 0
# 9 9 (0 + 9) (9)
# 50 41 (9 + 41) (41)
# 62 12 (12 + 50) (12)
# 65 3 (3 + 62) (3)
# 139 74 (74 + 63) (74)
# 154 15 (15 + 139) (15)
# After 154
