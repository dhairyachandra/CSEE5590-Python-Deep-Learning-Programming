# Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant
# string and print it.

name = input('Enter String: ')
short = name[2:]
string = short[::-1]
print(string)