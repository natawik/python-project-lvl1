from random import randint, choice
from operator import sub, add, mul


DESCRIPTION = 'What is the result of the expression?'


def make_round():
    expression, right_answer = generate_rand_exp()
    return expression, str(right_answer)


def generate_rand_exp():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    substraction = ('-', sub)
    addition = ('+', add)
    muptiplication = ('*', mul)
    operation, function = choice([substraction, addition, muptiplication])
    right_answer = function(num1, num2)
    show = '{} {} {}'
    return show.format(num1, operation, num2), right_answer
