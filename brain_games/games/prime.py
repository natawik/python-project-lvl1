from random import randint
from brain_games.games.even import compare


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_round():
    number = randint(1, 100)
    is_right = is_prime(number)
    right_answer = compare(is_right)
    return number, right_answer


def is_prime(number):
    if (number < 2):
        return True
    div = 2
    while(div <= number):
        if not number % div:
            div += 1
        return number == div
