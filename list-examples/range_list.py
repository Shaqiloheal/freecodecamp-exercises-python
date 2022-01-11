print(range(4))
# range(0, 4)

friends = ['Carol', 'Warren', 'Dougal']
print(len(friends))
# 3

print(range(len(friends)))
# range(0, 3)

for friend in friends:
    print('Happy New Year:', friend)
# Happy New Year: Carol
# Happy New Year: Warren
# Happy New Year: Dougal

# Another way of loop
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)