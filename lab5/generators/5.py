def down(n):
    i = n
    while(i >= 0):
        yield i
        i -= 1

n = int(input())

for i in down(n):
    print(i)