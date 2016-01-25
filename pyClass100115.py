__author__ = 'vikram'

from bank_account import BankAccount

account = BankAccount()
account.deposit(40)

print(account)

def exclude(pred_func, full_list):
    exc_list = []
    for n in full_list:
        if not pred_func(n):
            exc_list.append(n)
    return exc_list
print exclude(lambda x: len(x) > 3, ["red", "blue", "green"])
print exclude(bool, [False, True, False])

def call(some_func, *args):
    print args
    return some_func(*args)

print call(int)
print call(len, "hello")

