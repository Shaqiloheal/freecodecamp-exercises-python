def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Warren')
print(greet('es'), 'Carol')
print(greet('fr'), 'Vikki')

# The return statement ends the function execution
# and 'sends back' the result of the function.