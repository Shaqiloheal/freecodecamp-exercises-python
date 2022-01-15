abc = 'With three words'
stuff = abc.split()

print(stuff)
#['With', 'three', 'words']
print(len(stuff))
# 3
print(stuff[0])
# With

for w in stuff:
    print(w)
# With
# Three
# Words    