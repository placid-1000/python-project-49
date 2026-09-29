import prompt
from brain_games.cli import welcome_user

def main():
    # welcome_user() внутри себя уже спросит имя и скажет "Hello, {name}!"
    # Нам нужно только вывести заголовок проекта после этого.
    name = welcome_user()
    print(f"Welcome to the Brain Games, {name}!")

if __name__ == "__main__":
    main()
