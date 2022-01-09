fruit = 'banana'
'n' in fruit
# True

'm' in fruit
# False

'nan' in fruit
# True

if 'a' in fruit:
    print('Found it!')
# Found it!

word = 'banana'

if word == 'banana':
    print('All right, bananas.')
# All right, bananas.

word = 'banana' # increase or decrese the word to change to if or elif statement

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')
