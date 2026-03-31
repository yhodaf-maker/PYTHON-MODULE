from operator import mul, sub


def add(x, y):
    return x + y        

def subtract(x, y):
    return x - y    

def mult(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y        
    
    
def calculate(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Error: Unsupported operation"
    