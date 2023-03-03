import re 
n = str(input())
x = re.findall("a.{2,3}b", n)
print(x)