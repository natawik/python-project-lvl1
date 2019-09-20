from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_round():
    number = randint(1, 100)
    if is_even(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return number, right_answer


def is_even(number):
    if number % 2:
        return False
    return True
