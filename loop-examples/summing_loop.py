zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Before 0
# 9 9
# 50 41
# 62 12
# 65 3
# 139 74
# 154 15
# After 154
