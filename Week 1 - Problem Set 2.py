"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print, number of times bob occurs is: 2

"""

count = 0
x = 0
y = 1
z = 2
while (z < len(s)):
    if s[x] == "b" and s[y] == "o" and s[z] == "b":
        count += 1
    x += 1
    y += 1
    z += 1
print("Number of times bob occrus is:" + str(count))
