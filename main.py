import time
from terminal.cleaners import clear_screen, hide_cursor, show_cursor


def purpose_title():
    print("Memorize 🧠 Your Multiplication ✖️ Tables")
    print()


def expression_prompt(context: str):
    match context:
        case "quiz":
            return f"{digit_input} x {digit} = ?"
        case "normal":
            return f"{digit_input} x {digit} = {digit_input * digit}"


def timed_prompt(prompt: str, seconds: int, show_timer=False):
    if show_timer:
        for second in range(seconds):
            print(f"Timer: ({second})")
            print(prompt)
            clear_screen()
            time.sleep(seconds)
    else:
        print(prompt)
        clear_screen()
        time.sleep(seconds)


def display_current_score():
    global score
    global WIN_SCORE
    print(f"Score: {score}/{WIN_SCORE}")
    print()


WIN_SCORE = 10

score = 0
points_per_correct_answer = 1
points_lose_per_wrong_answer = 1

while True:
    purpose_title()
    digit_input = int(input("Digit: ").strip())
    clear_screen()

    purpose_title()
    for digit in range(1, 11):
        hide_cursor()
        display_current_score()
        print(expression_prompt(context="normal"))
        time.sleep(3)
        clear_screen()

        while True:
            display_current_score()
            print(expression_prompt(context="quiz"))
            print()
            show_cursor()
            answer = int(input("Answer from memory only: ").strip())
            clear_screen()
            hide_cursor()

            correct_answer = digit_input * digit
            score_change = 0

            if answer == correct_answer:
                score += points_per_correct_answer
                score_change += points_per_correct_answer
                display_current_score()
                print(
                    f"{answer} is correct! You earned {score_change} memory point{'' if score_change == 1 else 's'}!"
                )
            else:
                if score > 1:
                    score -= points_lose_per_wrong_answer
                    score_change -= points_lose_per_wrong_answer
                display_current_score()
                print(
                    f"{answer} is incorrect! Try again! {f'You lost {score_change} memory point{"" if score_change == 1 else "s"}!' if score > 1 else ''}"
                )
            input()
            clear_screen()

            if answer == correct_answer:
                break
