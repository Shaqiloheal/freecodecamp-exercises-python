count = 0
sum = 0
print('Before', count, sum)

for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

# count, sum, value
# 1 9 9
# 2 50 4
# 3 62 12
# 4 65 3
# 5 139 74
# 6 154 15
# count, sum, average
# 6 154 25.666666666666668