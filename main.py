import time
from terminal.cleaners import clear_screen, hide_cursor, show_cursor
from terminal.colors import Colors


def purpose_title():
    print("Memorize 🧠 Your Multiplication ✖️ Tables")
    print()


def expression_prompt(context: str):
    match context:
        case "quiz":
            return f"{digit_input} x {digit} = ?"
        case "normal":
            return f"{digit_input} x {digit} = {Colors.BOLD}{digit_input * digit}{Colors.END}"


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

    for digit in range(1, WIN_SCORE + 1):
        hide_cursor()

        while True:
            countdown = 3
            while countdown > 0:
                purpose_title()
                display_current_score()
                print(
                    f"Correct Answer View Timer ({Colors.BOLD}{countdown}{Colors.END})"
                )
                print(f"ANSWER VIEW: {expression_prompt(context="normal")}")
                time.sleep(1)
                countdown -= 1
                clear_screen()

            purpose_title()
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
                score_change = points_per_correct_answer
                purpose_title()
                display_current_score()
                print(
                    f"{answer} is correct! You earned {score_change} memory point{'' if score_change == 1 else 's'}!"
                )
                time.sleep(2)
                clear_screen()
                break
            else:
                if score > 1:
                    score -= points_lose_per_wrong_answer
                    score_change = points_lose_per_wrong_answer
                purpose_title()
                display_current_score()
                print(
                    f"{answer} is incorrect! Try again! {f'You lost {score_change} memory point{"" if score_change == 1 else "s"}!' if score > 1 else ''}"
                )
                time.sleep(2)
                clear_screen()

    else:
        while True:
            purpose_title()
            print(
                f"Congrats 🥳 on successfully memorizing the multiplication table of {digit_input} till {WIN_SCORE}!"
            )
            print()
            again = input(
                "Click 'Enter' to return to memorizing a table of another digit or q to quit"
            ).strip()
            clear_screen()

            if again == "q":
                purpose_title()
                print("Thanks for memorizing! Hope to see you again!")
                exit()
            elif again == "":
                break
