from random import randint


def show_progression():
    num_1 = randint(1, 100)
    step = randint(1, 10)
    prog_length = 1
    show_prog = ''
    while (prog_length <= 10):
        num_1 += step
        show_prog += str(num_1) + ' '
        prog_length += 1
    return show_prog


def hidden_number(condition):
    return condition.split(' ')[randint(0, 9)]


def hide_number(condition, right_answer):
    return condition.replace(right_answer, '..')
