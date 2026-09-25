import prompt
from brain_games.cli import welcome_user

ROUNDS_COUNT = 3

def run(game):
    name = welcome_user()
    print(game.DESCRIPTION)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
