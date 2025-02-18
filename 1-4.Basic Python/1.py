class InsufficientFundsError(Exception):
    pass

def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds")
    return balance - amount

try:
    print(withdraw(500, 100))  
    print(withdraw(500, 600))  
except InsufficientFundsError as e:
    print(e)
