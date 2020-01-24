#  Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex

str = "I love playing with Python"
spt = str.split()
result = list()
final = ""
print (spt)
for i in spt:
    if i == "Python":
        i = "Pythons"
    result.append(i)

for x in result:
    final += x
    final += " "

print(final)
