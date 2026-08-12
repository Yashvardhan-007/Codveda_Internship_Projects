# Codveda Level 1 - Task 1: Simple Calculator

A professional command-line calculator developed in Python for the **Codveda Technology Python Development Internship**.

## Internship Requirement

The official task requires:

- Functions for addition, subtraction, multiplication and division
- Two user inputs
- User-selected operation
- Appropriate handling of division by zero

This implementation satisfies those requirements and adds input validation, clean output, reusable functions, and automated tests.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero protection
- Invalid-number validation
- Invalid-operation validation
- Decimal arithmetic using Python's `decimal` module
- Interactive command-line interface
- Unit tests
- Clean project structure

## Technologies

- Python 3
- Standard Library
- `decimal`
- `unittest`

No third-party packages are required.

## Project Structure

```text
Codveda_Level1_Task1_Simple_Calculator/
│
├── calculator.py
├── test_calculator.py
├── README.md
└── .gitignore
```

## Requirements

Python 3.9+ is recommended.

Check your version:

```bash
python --version
```

## Run the Calculator

```bash
python calculator.py
```

On some systems:

```bash
python3 calculator.py
```

## Example

```text
=======================================================
              CODVEDA PYTHON CALCULATOR
=======================================================

Select an operation:
  1. Addition       (+)
  2. Subtraction    (-)
  3. Multiplication (*)
  4. Division       (/)
  5. Exit

Enter your choice: 4
Enter first number: 100
Enter second number: 4
Choose operation (1-4): 4

-------------------------------------------------------
Operation : Division
Expression: 100 / 4
Result    : 25
-------------------------------------------------------
```

## Error Handling

Example:

```text
Enter first number: 10
Enter second number: 0
Choose operation (1-4): 4

[ERROR] Cannot divide by zero.
```

Invalid input is also handled without crashing the program.

## Run Tests

```bash
python -m unittest -v
```

Expected result:

```text
Ran 9 tests ... OK
```

## Learning Outcomes

This project demonstrates:

- Python functions
- Dictionaries and function references
- Loops and conditionals
- Exception handling
- User input validation
- `Decimal` arithmetic
- Modular program design
- Unit testing
- Command-line application development

## Possible Future Enhancements

- Calculation history
- Scientific operations
- GUI using Tkinter
- Expression parser
- Export history to CSV/JSON
- Logging
- Configuration file

## Author

**Yashvardhan Singh**

Python Development Intern  
Codveda Technologies
