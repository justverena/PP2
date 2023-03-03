import re
n = str(input())
x = re.sub("\s",",", n) 
x1 = re.sub("\.",":", x)
print(x1)