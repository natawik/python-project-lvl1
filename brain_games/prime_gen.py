from random import randint


def show_rand_number():
    number = randint(1, 100)
    return number


def is_prime(number):
    if (number < 2):
        return True
    div = 2
    while(div <= number / 2):
        if (number % div == 0):
            return False
        div += 1
    return True


def right_answer(number):
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
