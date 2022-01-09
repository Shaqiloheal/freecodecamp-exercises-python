# Author: Warren Spalding (Shaqiloheal)
# Date: 09/01/2022
# Program which repeatedly reads numbers until the user enters "done".
# Prints out the total, count, and average of the numbers. If the user
# enters anything other than a number and error message appears and skips
# to the next number.

count = 0
total = 0.0

while True:
    value = input("Please input a number or input 'done' to finish: ")
    if value == 'done': # Breaks out loop when input is 'done'.
        break
    # Checks the value type.
    try:
        value = float(value)
    # Anything other than a float value will display this error message to the user.
    except:
        print("Please enter a numerical value.")
        continue # Continues the loop after the error.
    print(value)
    count = count + 1
    total = total + value
print("Finished!:")
# Count total: '#' - Total value: '#' - Average value: '#'
print("Count total:",count,"- Total value: ", total,"- Average value:", total / count)


