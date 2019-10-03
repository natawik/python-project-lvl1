from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def make_round():
    progression, right_answer = show_progression()
    return progression, str(right_answer)


def show_progression():
    num1 = randint(1, 100)
    step = randint(1, 10)
    rand_place = randint(1, 10)
    prog_length = 1
    show_prog = ''
    while prog_length <= 10:
        if prog_length != rand_place:
            show_prog += str(num1) + ' '
            prog_length += 1
            num1 += step
        else:
            show_prog += '..' + ' '
            prog_length += 1
            hidden_num = num1
            num1 += step
    return show_prog, hidden_num
