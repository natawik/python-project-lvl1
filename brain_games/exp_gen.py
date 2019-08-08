from random import randint, choice
import brain_games.convertation_str_to_num


def show_rand_expression():
    exp_gen = (randint(1, 100), choice(['-', '+', '*']), randint(1, 100))
    (num_1, operation, num_2) = exp_gen
    show = '{} {} {}'
    return (show.format(num_1, operation, num_2))


def rand_expression(exp):
    num_1 = brain_games.convertation_str_to_num.conv_num_1(exp)
    num_2 = brain_games.convertation_str_to_num.conv_num_2(exp)
    if '-' in exp:
        right_answer = num_1 - num_2
    elif '+' in exp:
        right_answer = num_1 + num_2
    else:
        right_answer = num_1 * num_2
    return right_answer
