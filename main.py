import math


class Calculator:
    def __init__(self):
        """Set up the dictionary with the basic operations from the original program."""
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }

    def add_operation(self, symbol, function):
        """Add a new operation symbol and its function to the dictionary."""
        self.operations[symbol] = function

    def calculate(self, num1, symbol, num2):
        """Validate the inputs, then run the matching operation."""
        # Check that both inputs are numbers
        for value in (num1, num2):
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                message = f"Error: '{value}' is not a valid number."
                print(message)
                raise TypeError(message)

        # Check that the operator is valid
        if symbol not in self.operations:
            valid = ", ".join(self.operations)
            message = f"Error: Invalid operator entered. Please use one of: {valid}"
            print(message)
            raise ValueError(message)

        # Run the operation, catching math errors
        try:
            return self.operations[symbol](num1, num2)
        except ZeroDivisionError:
            message = "Error: Division by zero is not allowed."
            print(message)
            raise
        except ValueError as e:
            message = f"Error: Invalid input for this operation ({e})."
            print(message)
            raise
        except OverflowError:
            message = "Error: The result is too large to calculate."
            print(message)
            raise


# ---- Advanced operations ----

def exponentiation(base, exponent):
    return math.pow(base, exponent)


def square_root(number, _unused=None):
    """Square root of the first number; the second number is ignored."""
    return math.sqrt(number)


def logarithm(number, base):
    """Logarithm of number in the given base."""
    return math.log(number, base)


# ---- Main program ----

if __name__ == "__main__":
    calc = Calculator()
    calc.add_operation("**", exponentiation)
    calc.add_operation("sqrt", square_root)
    calc.add_operation("log", logarithm)

    print("Welcome to the Advanced Calculator!")
    print("Operators: +  -  *  /  **  sqrt  log")
    print("(For sqrt the second number is ignored; for log it is the base.)")

    while True:
        try:
            n1 = float(input("\nEnter the first number: "))
            operator = input("Enter the operator: ").strip()
            n2 = float(input("Enter the second number: "))

            result = calc.calculate(n1, operator, n2)
            print(f"The result is: {result}")

        except ValueError:
            # Covers non-numeric input from float() and errors raised by calculate()
            print("Please try again with valid values.")
        except (TypeError, ZeroDivisionError, OverflowError):
            print("Please try again with valid values.")

        cont = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if cont != "yes" and cont != "y":
            print("Thank you for using the calculator. Goodbye")
            break