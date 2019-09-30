from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_round():
    number = randint(1, 100)
    right_answer = as_yes_or_no(is_even(number))
    return number, right_answer


def is_even(number):
    if number % 2:
        return False
    return True


def as_yes_or_no(is_right):
    if is_right:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
