from random import randint


def show_progression():
    num_1 = randint(1, 100)
    step = randint(1, 10)
    progr_length = 1
    show_progr = ''
    while (progr_length <= 10):
        num_1 += step
        show_progr += str(num_1) + ' '
        progr_length += 1
    return show_progr


def hidden_number(progression):
    return progression.split(' ')[randint(0, 9)]


def hide_number(progression, right_answer):
    return progression.replace(right_answer, '..')
