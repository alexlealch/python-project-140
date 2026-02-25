import random

from brain_games.cli import welcome_user


def run_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_count = 0
    while rounds_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")

        expected_answer = "yes" if number % 2 == 0 else "no"

        if answer == expected_answer:
            print("Correct!")
            rounds_count += 1
        else:
            message = f"'{answer}' is wrong answer ;(. "
            message += f"Correct answer was '{expected_answer}'."
            print(message)
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == "__main__":
    main()
