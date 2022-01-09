# Author: Warren Spalding (Shaqiloheal)
# Date: 09/01/2022
# Program that takes the following Python string and uses the find
# function and string slicing to extract the poerion of the string
# after the colon character and then use the float function to
# convert the extracted string into a floating point number.

string_1 = 'X-DSPAM-Confidence: 0.8475'

colon_num = string_1.find(':')

colon_numfloat = string_1[colon_num + 2 :]
print(type(colon_numfloat))
# <type 'str'>

colon_numfloat = float(colon_numfloat)
print(colon_numfloat)
# 0.8475
print(type(colon_numfloat)) # Print used due to Visual Studio Code settings.
# <class 'float'>
