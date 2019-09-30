from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_round():
    number = randint(1, 100)
    is_right = is_even(number)
    right_answer = compare(is_right)
    return number, right_answer


def is_even(number):
    if number % 2:
        return False
    return True


def compare(is_right):
    if is_right:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
