list = [int(x) for x in input().split()]
def filter(a):
    for i in range(2, a-1):
        if a % i == 0:
            return False
    return True
for i in range(len(list)):
    if filter(list[i]):
        print(list[i], end=" ")