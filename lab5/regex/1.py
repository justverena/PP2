import re
n = str(input())
x = re.findall('a.*b', n)
print(x)