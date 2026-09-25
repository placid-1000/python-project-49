import random

RULE = 'What is the result of the expression?'


def generate_round():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)

    question = f'{a} {operation} {b}'

    match operation:
        case '+':
            answer = str(a + b)
        case '-':
            answer = str(a - b)
        case '*':
            answer = str(a * b)

    return question, answer
