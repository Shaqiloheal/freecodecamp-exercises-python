str1 = "Hello"
str2 = 'there'
bob = str1 + str2 # '+' means concentrate
print(bob)
# Hello there

str3 = '123'
#str3 = str3 + 1
#Causes Traceback TypeError as it cannot concentrate str and int objects

x = int(str3) + 1 # converts the string into a integer
print(x)
# 124