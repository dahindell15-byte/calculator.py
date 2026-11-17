"""A simple, beginner-friendly command-line calculator."""

import math


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference between two numbers."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Return the quotient, or raise an error if dividing by zero."""
    if second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first_number / second_number


# Each menu choice is linked to its display name and operation function.
OPERATIONS = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
}


def get_number(prompt):
    """Ask for a finite number, repeating until the input is valid."""
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not math.isfinite(number):
            print("Please enter a finite number.")
            continue

        return number


def get_operation_choice():
    """Show the menu and return a valid choice, or None to exit."""
    while True:
        print("\nChoose an operation:")
        for choice, (name, _) in OPERATIONS.items():
            print(f"{choice}. {name}")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice in OPERATIONS:
            return choice
        if choice == "5":
            return None

        print("Please choose a valid option from 1 to 5.")


def main():
    """Display the menu and run calculations until the user chooses to exit."""
    print("Welcome to the Calculator!")

    try:
        while True:
            choice = get_operation_choice()
            if choice is None:
                print("Goodbye!")
                break

            first_number = get_number("Enter the first number: ")
            second_number = get_number("Enter the second number: ")
            operation_name, operation_function = OPERATIONS[choice]

            try:
                result = operation_function(first_number, second_number)
            except ZeroDivisionError as error:
                print(error)
                continue

            print(f"{operation_name} result: {result:g}")
    except EOFError:
        print("\nInput ended. Goodbye!")


if __name__ == "__main__":
    main()