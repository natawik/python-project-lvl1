from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_round():
    number = randint(1, 100)
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return number, right_answer


def is_prime(number):
    if (number < 2):
        return True
    div = 2
    while(div <= number):
        if not number % div:
            div += 1
        return number == div
