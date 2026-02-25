import operator
import random

from brain_games.cli import welcome_user


def run_game():
    name = welcome_user()
    print("What is the result of the expression?")

    rounds_count = 0
    while rounds_count < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        simbol = random.choice(["+", "-", "*"])
        expression = f"{number1} {simbol} {number2}"
        print(f"Question: {expression}")
        answer = input("Your answer: ")

        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
        }

        expected_answer = operations[simbol](number1, number2)

        if answer == str(expected_answer):
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
