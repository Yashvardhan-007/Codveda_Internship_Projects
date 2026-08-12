"""
Codveda Technology - Python Development Internship
Level 1 - Task 1: Simple Calculator

The core requirements from the internship task are:
- Separate functions for each operation
- Two user inputs
- Operation selection
- Division-by-zero handling
"""

from decimal import Decimal, InvalidOperation


def add(a: Decimal, b: Decimal) -> Decimal:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Return the product of two numbers."""
    return a * b


def divide(a: Decimal, b: Decimal) -> Decimal:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
}


def parse_number(value: str) -> Decimal:
    """Convert user input into a Decimal with a friendly error."""
    try:
        return Decimal(value.strip())
    except InvalidOperation as exc:
        raise ValueError(f"'{value}' is not a valid number.") from exc


def format_number(value: Decimal) -> str:
    """Format Decimal output cleanly for the CLI."""
    if value == value.to_integral_value():
        return str(value.quantize(Decimal("1")))
    return format(value.normalize(), "f")


def calculate(operation: str, a: Decimal, b: Decimal) -> Decimal:
    """Perform the selected calculation."""
    if operation not in OPERATIONS:
        raise ValueError("Invalid operation. Choose 1, 2, 3, or 4.")

    _, function = OPERATIONS[operation]
    return function(a, b)


def print_banner() -> None:
    print("\n" + "=" * 55)
    print("              CODVEDA PYTHON CALCULATOR")
    print("=" * 55)


def print_menu() -> None:
    print("\nSelect an operation:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Exit")


def run_calculation() -> None:
    """Read inputs, calculate, and display the result."""
    try:
        first = parse_number(input("Enter first number: "))
        second = parse_number(input("Enter second number: "))
    except ValueError as error:
        print(f"\n[ERROR] {error}")
        return

    operation = input("Choose operation (1-4): ").strip()

    if operation not in OPERATIONS:
        print("[ERROR] Invalid operation. Please choose 1, 2, 3, or 4.")
        return

    name, _ = OPERATIONS[operation]

    try:
        result = calculate(operation, first, second)
    except ZeroDivisionError as error:
        print(f"\n[ERROR] {error}")
        return

    print("\n" + "-" * 55)
    print(f"Operation : {name}")
    print(f"Expression: {format_number(first)} {operation_symbol(operation)} "
          f"{format_number(second)}")
    print(f"Result    : {format_number(result)}")
    print("-" * 55)


def operation_symbol(operation: str) -> str:
    """Return the mathematical symbol for an operation."""
    return {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
    }[operation]


def main() -> None:
    """Run the calculator until the user chooses Exit."""
    print_banner()

    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "5":
            print("\nThank you for using the Codveda Calculator. Goodbye!")
            break

        if choice in OPERATIONS:
            run_calculation()
        else:
            print("[ERROR] Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()
