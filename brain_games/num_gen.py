from random import randint


def show_rand_number():
    number = randint(1, 100)
    return number


def is_even_number(number):
    if (number % 2 == 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
