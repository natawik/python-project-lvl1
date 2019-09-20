from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def make_round():
    expression, num1, num2 = show_rand_expression()
    if '-' in expression:
        right_answer = int(num1) - int(num2)
    elif '+' in expression:
        right_answer = int(num1) + int(num2)
    else:
        right_answer = int(num1) * int(num2)
    return expression, str(right_answer)


def show_rand_expression():
    num1 = randint(1, 100)
    operation = choice(['-', '+', '*'])
    num2 = randint(1, 100)
    show = '{} {} {}'
    return show.format(num1, operation, num2), num1, num2
