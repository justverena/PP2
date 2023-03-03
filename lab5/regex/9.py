import re
n = input()
x = re.sub(r"(\w)([A-Z])", r"\1 \2", n)
print(x)