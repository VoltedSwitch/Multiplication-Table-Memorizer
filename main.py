import time
import sys
import termios
from terminal.cleaners import clear_screen, hide_cursor, show_cursor
from terminal.colors import Colors


def purpose_title():
    print("Memorize 🧠 Your Multiplication ✖️ Tables")
    print()


def expression_prompt(context: str):
    match context:
        case "quiz":
            return f"{digit_input} x {digit} ="
        case "normal":
            return f"{digit_input} x {digit} = {Colors.BOLD}{Colors.UNDERLINE}{digit_input * digit}{Colors.END}"


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
    print(f"Score: {score}/{WIN_SCORE}, {WIN_SCORE} to win!")
    print()


def always_display():
    purpose_title()
    display_current_score()


def discard_pending_input():
    """Drop keys typed during the answer-view countdown."""
    if sys.stdin.isatty():
        termios.tcflush(sys.stdin.fileno(), termios.TCIFLUSH)


WIN_SCORE = 10

score = 0
points_per_correct_answer = 1
points_lose_per_wrong_answer = 1

clear_screen()

while True:
    purpose_title()
    digit_input = int(input("Digit: ").strip())
    clear_screen()

    for digit in range(1, WIN_SCORE + 1):
        hide_cursor()

        while True:
            countdown1 = 3
            while countdown1 > 0:
                always_display()
                print(
                    f"Correct Answer View Timer ({Colors.BOLD}{countdown1}{Colors.END})"
                )
                print(f"ANSWER VIEW: {expression_prompt(context="normal")}")
                time.sleep(1)
                countdown1 -= 1
                clear_screen()

            countdown2 = 5

            while countdown2 > 0:
                always_display()
                print(
                    f"Keep correct answer to {digit_input} x {digit} in mind\nuntil quiz prompt appears! Timer ({Colors.BOLD}{countdown2}{Colors.END})"
                )
                time.sleep(1)
                countdown2 -= 1
                clear_screen()

            discard_pending_input()
            show_cursor()
            while True:
                always_display()
                answer = input(f"{expression_prompt(context="quiz")} ").strip()
                print()
                clear_screen()
                if answer.isdigit():
                    answer = int(answer)
                    break
            hide_cursor()

            correct_answer = digit_input * digit
            score_change = 0

            if answer == correct_answer:
                score += points_per_correct_answer
                score_change = points_per_correct_answer
                always_display()
                print(
                    f"Correct! {digit_input} x {digit} = {Colors.BOLD + Colors.UNDERLINE}{answer}{Colors.END}!\nYou earned {score_change} memory point{'' if score_change == 1 else 's'}!"
                )
                time.sleep(3)
                clear_screen()
                break
            else:
                always_display()
                print(f"{answer} is incorrect! Try again!")
                time.sleep(2)
                clear_screen()
    else:
        while True:
            show_cursor()
            always_display()
            print(
                f"Congrats 🥳 on your win to attempt to memorize the multiplication table of {digit_input} till {WIN_SCORE}!"
            )
            print()
            again = input(
                "Click 'Enter' to return to memorizing a table of another digit or q to quit"
            ).strip()
            clear_screen()

            if again == "q":
                always_display()
                print("Thanks for memorizing! Hope to see you again!")
                exit()
            elif again == "":
                score = 0
                break
