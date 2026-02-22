from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import run_game as brain_even
from brain_games.scripts.brain_calc import run_game as brain_calc
from brain_games.scripts.brain_gcd import run_game as brain_gcd
from brain_games.scripts.brain_progression import run_game as brain_progression


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    print("Which game would you like to play?")
    print("1. Even or Odd")
    print("2. Calculator")
    print("3. GCD")
    print("4. Progression")
    choice = input("Your choice: ")
    if choice == "1":
        brain_even()
    elif choice == "2":
        brain_calc()
    elif choice == "3":
        brain_gcd()
    elif choice == "4":
        brain_progression()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
