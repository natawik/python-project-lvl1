from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_round():
    two_rand_numbers, num1, num2 = show_two_rand_numbers()
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
        right_answer = num1
    return two_rand_numbers, str(right_answer)


def show_two_rand_numbers():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    show = '{} {}'
    return show.format(num1, num2), num1, num2
