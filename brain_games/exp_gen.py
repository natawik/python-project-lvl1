from random import randint, choice


def show_rand_expression():
    exp_gen = (randint(1, 100), choice(['-', '+', '*']), randint(1, 100))
    (num_1, operation, num_2) = exp_gen
    show = '{} {} {}'
    return (show.format(num_1, operation, num_2))


def conv_num_1(exp):
    i = 0
    num_1 = ''
    while(exp[i] != ' '):
        num_1 += exp[i]
        i += 1
    return int(num_1)


def conv_num_2(exp):
    i = -1
    num_2 = ''
    while(exp[i] != ' '):
        num_2 += exp[i]
        i -= 1
    num_2 = num_2[::-1]
    return int(num_2)


def rand_expression(exp):
    num_1 = conv_num_1(exp)
    num_2 = conv_num_2(exp)
    if '-' in exp:
        right_answer = num_1 - num_2
    elif '+' in exp:
        right_answer = num_1 + num_2
    else:
        right_answer = num_1 * num_2
    return right_answer