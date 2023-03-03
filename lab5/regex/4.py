import re 
n = str(input())
x = re.findall("[A-Z][a-z]+", n)
print(x)