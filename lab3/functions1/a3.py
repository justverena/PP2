def solve(numheads, numlegs):
    c = numheads * 2
    r = (numlegs - c) / 2
    c = numheads - r
    print("chikens :", c)
    print("rabbits :", r)
numheads = 35
numlegs = 94
solve(numheads, numlegs)