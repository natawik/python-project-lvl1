from random import randint
from brain_games.common_function import as_yes_or_no


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_round():
    number = randint(1, 100)
    return number, as_yes_or_no(is_even(number))


def is_even(number):
    if number % 2:
        return False
    return True
