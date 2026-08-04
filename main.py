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


if __name__ == "__main__":
    print("Welcome to the Simple Calculator!")
    
    while True:
        try:
           
            n1 = float(input("\nEnter the first number: "))
            n2 = float(input("Enter the second number: "))
            
            result = calculator(n1, n2)
            print(f"The result is: {result}")
            
        except ValueError:
            print("Error: Please enter valid numeric values for the numbers.")
    
        cont = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes' and cont != 'y':
            print("Thank you for using the calculator. Goodbye")
            break

