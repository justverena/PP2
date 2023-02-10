def spygame(list):
    for i in range(len(list)):
        if list[i]==0 and list[i+1]==0 and list[i+2]==7:
            return True
    return False
print(spygame([1,2,4,0,0,7,5]))
print(spygame([1,0,2,4,0,5,7])) 
print(spygame([1,7,2,0,4,5,0])) 