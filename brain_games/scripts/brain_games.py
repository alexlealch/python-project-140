from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import is_even_or_odd


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    is_even_or_odd()


if __name__ == "__main__":
    main()
