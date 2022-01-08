zork = 0 # Beginning of counter
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1 # counter increases by 1 each time
    print(zork, thing)
print('After', zork)

# Before 0
# 1 9
# 2 41
# 3 12
# 4 3
# 5 74
# After 6