from random import randint, choice
import brain_games.games.convert_str_to_num


def show_rand_expression():
    exp_gen = (randint(1, 100), choice(['-', '+', '*']), randint(1, 100))
    (num_1, operation, num_2) = exp_gen
    show = '{} {} {}'
    return (show.format(num_1, operation, num_2))


def rand_expression(condition):
    num_1 = brain_games.games.convert_str_to_num.conv_num_1(condition)
    num_2 = brain_games.games.convert_str_to_num.conv_num_2(condition)
    if '-' in condition:
        right_answer = num_1 - num_2
    elif '+' in condition:
        right_answer = num_1 + num_2
    else:
        right_answer = num_1 * num_2
    return right_answer
