# Lists index their entries based on the position
# in the list.  Variables inside the dictionary are
# allocated with a "lookup tag".

bag = dict()
bag['money'] = 12
bag['sweets'] = 3
bag['laptop'] = 75
print(bag)
# {'money': 12, 'sweets': 3, 'laptop': 75}

print(bag['sweets'])
# 3

bag['sweets'] = bag['sweets'] + 2
print(bag)
# {'money': 12, 'sweets': 5, 'laptop': 75}
