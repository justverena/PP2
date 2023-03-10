import time
import math
n = float(input())
mil = int(input())
time.sleep(mil / 1000)
nsqrt = math.sqrt(n)
print("The square root of " , n , " after " , mil , " milliseconds is " , nsqrt)