import random
n = random.randint(1, 20)
tr = 0
print("Hello! What is your name?")
k = input()
print("Well, " , k, ", I am thinking of a number between 1 and 20.")
print("Take a guess.")
n1 = int(input())
while (n1 != n):
    if (n1 < n):
        print("Your guess is too low.")
    elif (n1 > n):
        print("Your guess is too high.")
    print("Take a guess.")
    tr += 1
    n1 = int(input())
print("Good job, ", k, "! You guessed my number in ", tr, " guesses!")