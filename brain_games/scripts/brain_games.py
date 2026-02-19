from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import is_even_or_odd
from brain_games.scripts.brain_calc import brain_calc


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    print("Which game would you like to play?")
    print("1. Even or Odd")
    print("2. Calculator")
    choice = input("Your choice: ")
    if choice == "1":
        is_even_or_odd()
    elif choice == "2":
        brain_calc()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
