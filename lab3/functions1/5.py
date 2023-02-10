from itertools import permutations
def perm(k):
    k1 = list(permutations(k))
    for i in k1:
        print(i)
        
k = (str(input()))
perm(k)