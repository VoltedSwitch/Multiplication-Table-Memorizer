from terminal.cleaners import clear_screen


def purpose_title():
    print("Memorize 🧠 Your Multiplication ✖️ Tables")
    print()


while True:
    purpose_title()
    digit_input = int(input("Digit: ").strip())
    clear_screen()

    purpose_title()
    for digit in range(1, 11):
        print(f"{digit_input} x {digit} = {digit_input * digit}")
        print()
        memorized_input = input(
            "Quiz me on this expression, Press 'Enter' to proceed: "
        ).strip()
        clear_screen()
