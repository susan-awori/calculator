# Advanced Calculator

A command-line calculator built with object-oriented Python. It expands on an earlier basic calculator by adding a `Calculator` class, advanced math operations, and error handling.

## Features

- Basic operations: addition, subtraction, multiplication, division
- Advanced operations: exponentiation, square root, logarithm
- Operations are stored in a dictionary, so new ones can be added with `add_operation`
- Input validation using `isinstance()` and exceptions for invalid numbers, invalid operators, division by zero, and math domain errors
- Interactive loop that runs until the user chooses to exit

## Requirements

- Python 3.8 or newer
- No external packages (uses the built-in `math` module)

## Usage

```bash
python calculator.py
```

Enter the first number, the operator, and the second number when prompted.

| Operator | Operation | Notes |
|----------|-----------|-------|
| `+` `-` `*` `/` | Basic arithmetic | |
| `**` | Exponentiation | first number is the base, second is the exponent |
| `sqrt` | Square root | second number is ignored |
| `log` | Logarithm | second number is the base |

### Example

```
Welcome to the Advanced Calculator!

Enter the first number: 8
Enter the operator: log
Enter the second number: 2
The result is: 3.0
```

## Project Structure

- `Calculator` class:
  - `__init__()` sets up the operations dictionary with `+ - * /`
  - `add_operation(symbol, function)` registers a new operation
  - `calculate(num1, symbol, num2)` validates input, runs the operation, and raises an exception on error
- `exponentiation()`, `square_root()`, `logarithm()` are the advanced operation functions
- The main program creates a `Calculator`, registers the advanced operations, and runs the input loop

## Adding a New Operation

Write a function that takes two arguments and register it:

```python
def modulus(a, b):
    return a % b

calc = Calculator()
calc.add_operation("%", modulus)
```

## Error Handling

`calculate` prints an error message and raises an exception for:

- Non-numeric input (`TypeError`)
- Unsupported operator (`ValueError`)
- Division by zero (`ZeroDivisionError`)
- Invalid math input such as `sqrt` of a negative number (`ValueError`)
- Results too large to compute (`OverflowError`)

