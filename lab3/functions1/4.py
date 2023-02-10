def filter_prime(k):
    if( k <=1):
     return False
    else:
        for i in range(2, k):
          if( k % i == 0):
              return False
    return True
k = int(input())
print(filter_prime(k))