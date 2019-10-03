from random import randint
from brain_games.help_function import as_yes_or_no


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_round():
    number = randint(1, 100)
    return number, as_yes_or_no(is_prime(number))


def is_prime(number):
    if (number < 2):
        return True
    div = 2
    while number % div:
        div += 1
    return number == div
