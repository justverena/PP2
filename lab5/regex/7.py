import re
n = input()
def snaketocamel(l):
    x = re.findall("[a-z]+", n)
    y = ""
    for i in x:
        y += i[0].upper() + i[1 : len(i)]
    return y

print(snaketocamel(n))