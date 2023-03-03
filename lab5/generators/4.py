def sq(x, y):
    for n in range(x, y + 1):
        yield n ** 2

x = int(input())

y = int(input())

for i in sq(x, y):
    print(i)