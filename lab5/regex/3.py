import re
n = str(input())
x = re.findall("^[a-z]+_[a-z]+$", n)
print(x)