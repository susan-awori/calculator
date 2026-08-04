def calculator(num1, num2):
    """
    Performs basic arithmetic operations (+, -, *, /) on two numbers 
    based on user input.
    """
    operator = input("Enter the operator (+, -, *, /): ").strip()
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
    
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operator entered. Please use +, -, *, or /."

