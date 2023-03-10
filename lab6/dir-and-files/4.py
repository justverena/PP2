import os
p = r'C:\Users\ASUS\Desktop\study\PP2\lab6\dir-and-files\fourth.txt'
file = open(p, "r")
l = 0
for i in file:
    if(i != '\n'):
        l += 1
print(l)