def even(n):
    i=0
    while(i%2==0 and i<=n):
        yield i
        i=i+2
    
n=int(input())

print(*even(n), sep=', ')