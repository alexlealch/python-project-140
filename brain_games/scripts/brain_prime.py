import math
import random

from brain_games.cli import welcome_user


def run_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    rounds_count = 0

    while rounds_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")

        if number < 2:
            is_prime = False
        else:
            is_prime = True
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    is_prime = False
                    break

        expected_answer = "yes" if is_prime else "no"
        if answer == expected_answer:
            print("Correct!")
            rounds_count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == "__main__":
    main()
