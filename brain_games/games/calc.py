import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)

    question = f'{first_number} {operation} {second_number}'

    match operation:
        case '+':
            answer = str(first_number + second_number)
        case '-':
            answer = str(first_number - second_number)
        case '*':
            answer = str(first_number * second_number)

    return question, answer
