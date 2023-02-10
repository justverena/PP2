def has_33(k):
    count = 0
    for i in range(len(k)):
        if(k[i] == 3 and k[i + 1] == 3):
            count += 1
    if(count > 0):
     return True
    else:
        return False

print(has_33([1, 3, 3]))    
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 