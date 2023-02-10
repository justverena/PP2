class BankAccount:
    def __init__(s):
        balance = float(input())
        s.balance = balance
    
    def depos(s):
        dep = float(input())
        s.balance += dep
        print("Your balance:", s.balance)
    def withdraw(s):
        wdr = int(input())
        if wdr <= s.balance:
            s.balance -= wdr
            print("Your balance has been successfully withdrawn!")
        else:
            print("Insufficient balance")
    def urbalnc(s):
        print("Your balance:", s.balance)

bnk = BankAccount()
bnk.depos()
bnk.withdraw()
bnk.urbalnc()