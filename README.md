# Multiplication Table Memorizer

A small terminal program that helps you memorize a multiplication table through timed answer previews and a recall quiz.

## Requirements

- Python 3.10 or newer (the program uses `match` statements)
- A terminal that supports ANSI escape codes

## Run

From the project directory, run:

```bash
python3 main.py
```

Enter a number when prompted. For each multiplier from 1 to 10, the program shows the answer briefly, gives you time to remember it, then asks you to enter the product from memory. Incorrect answers are repeated until correct. After completing the table, press Enter to choose another number or enter `q` to quit.

## Project files

- `main.py` — quiz flow and prompts
- `terminal/colors.py` — ANSI text styling
- `terminal/cleaners.py` — terminal screen and cursor helpers
