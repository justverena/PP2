p = r'C:\Users\ASUS\Desktop\study\PP2\lab6\dir-and-files\fifth.txt'
llist = ['text', 'and', 'text']
file = open(p, "w")
for i in llist:
    file.write(i + ' ')
file.close()
file = open(p, "r")
print(file.read())