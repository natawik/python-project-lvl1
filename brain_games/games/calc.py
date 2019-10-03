from random import randint, choice
from operator import sub, add, mul


DESCRIPTION = 'What is the result of the expression?'


def make_round():
    expression, right_answer = generate_rand_exp()
    return expression, str(right_answer)


def generate_rand_exp():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    substraction = ('-', sub(num1, num2))
    addition = ('+', add(num1, num2))
    muptiplication = ('*', mul(num1, num2))
    operation, right_answer = choice([substraction, addition, muptiplication])
    show = '{} {} {}'
    return show.format(num1, operation, num2), right_answer
