# Python Command-Line Calculator

A beginner-friendly calculator built with Python. It provides a simple terminal menu for the four basic arithmetic operations, validates user input, and keeps running until the user chooses to exit.

## Features

- Addition, subtraction, multiplication, and division
- Interactive menu with an Exit option
- Repeats calculations without restarting the program
- Validates menu choices and numeric input
- Rejects non-finite values such as `NaN` and infinity
- Handles division by zero without terminating the program
- Uses small, clearly named functions to keep the code approachable

## Technologies

- **Python 3**
- **Python standard library** (`math`); no third-party packages are required

## Project structure

```text
calculator.py/
├── calculator.py   # Calculator operations, input handling, and menu
└── README.md       # Project documentation
```

## Installation

1. Install Python 3 from [python.org](https://www.python.org/downloads/) if it is not already installed.
2. Clone this repository or download the project files.
3. Open the project folder in VS Code or a terminal.

There are no additional packages to install.

## Run the application

From the project directory, run:

```bash
python calculator.py
```

On some Windows installations, use:

```powershell
py calculator.py
```

Choose an operation from the menu, enter two numbers when prompted, and repeat as desired. Choose **5** to exit.

## Testing

The project does not currently include an automated test suite. The application has been manually exercised for all four operations, invalid menu choices, invalid and non-finite numeric input, division by zero, repeated calculations, and exiting.

To check the file's syntax with Python, run:

```bash
python -m py_compile calculator.py
```

## Future improvements

- Add automated unit tests for each operation and input-validation path
- Support calculation history
- Add configurable rounding or number formatting
- Provide a graphical user interface
- Add continuous integration to run tests automatically

## License

No license has been specified yet. Add a `LICENSE` file before redistributing this project if you want to grant others explicit reuse rights.
