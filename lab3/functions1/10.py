def unique(k) :
    k1 = []
    for a in k :
        if a not in k1 :
            k1.append(a)
    print(k1)

string = input()
k = string.split()
unique(k)