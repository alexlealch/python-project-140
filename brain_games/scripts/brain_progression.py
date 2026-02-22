import random


def run_game():
    print("What number is missing in the progression?")

    rounds_count = 0
    while rounds_count < 3:
        leng = random.randint(5, 10)
        start = random.randint(1, 10)
        step = random.randint(1, 10)
        stop = start + (step * leng)

        progression = list(range(start, stop, step))

        missing_index = random.randint(0, leng - 1)
        hidden_number = progression[missing_index]
        progression[missing_index] = ".."

        print(f"Question: {' '.join(map(str, progression))}")
        answer = input("Your answer: ")

        if int(answer) == hidden_number:
            print("Correct!")
            rounds_count += 1
        else:
            print(f"Wrong answer ;(. Correct answer was '{hidden_number}'.")
            break

    if rounds_count == 3:
        print("Congratulations!")


def main():
    run_game()


if __name__ == "__main__":
    main()
