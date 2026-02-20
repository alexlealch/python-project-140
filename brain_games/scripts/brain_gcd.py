import random
import math


def run_game():
    print("Find the greatest common divisor of given numbers.")

    rounds_count = 0

    while rounds_count < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f"Question: {number1} and {number2}")

        answer = input("Your answer: ")
        expected_answer = math.gcd(number1, number2)

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
