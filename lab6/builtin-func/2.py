s = str(input())
l , up = 0 , 0
i = 0
while(i < len(s)):
    if (s[i].islower()):
        l += 1
    elif (s[i].isupper()):
        up += 1
    i+=1
print(l , up)