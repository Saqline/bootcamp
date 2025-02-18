def calculate(num1: float, num2: float, operator: str) -> float:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

# Example usage
print(calculate(10, 5, '+'))  
print(calculate(10, 5, '-')) 
print(calculate(10, 5, '*')) 
print(calculate(10, 5, '/')) 
