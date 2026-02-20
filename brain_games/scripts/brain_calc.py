import random
import operator


def run_game():
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
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'."
            )
            print("Let's try again!")
            return

    print("Congratulations!")


def main():
    run_game()


if __name__ == "__main__":
    main()
