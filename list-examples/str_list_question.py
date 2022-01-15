words = 'His e-mail is q-lar@freecodecamp.org'

pieces = words.split() # splits whitespace
print(pieces)
# ['His', 'e-mail', 'is', 'q-lar@freecodecamp.org']

parts = pieces[3].split('-') # splits '- from 3rd index ('q-lar@freecodecamp.org')
print(parts)
# ['q', 'lar@freecodecamp.org']

n = parts[1] # selects index 1 ('lar@freecodecamp.org')
print(n)
# lar@freecodecamp.org