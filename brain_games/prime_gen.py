from random import randint


def show_rand_number():
    number = randint(1, 100)
    return number


def is_prime(number):
    if (number <= 2):
        return True
    elif (number > 2):
        div = 2
        while(number % div != 0):
            div += 1
            if (div == number):
                return True
        return False


def right_answer(number):
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
