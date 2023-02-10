def palindrome(k):
    count  = 0
    for i in range(len(k)):
        if(k[i]== k[len(k) - 1 - i]):
            count += 1
    if(count == len(k)):
       return True
    else:
        return False
k = str(input())
print(palindrome(k))