import brain_games.games.rand_number


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_round():
    number = brain_games.games.rand_number.rand_number()
    if is_even_number(number):
        right_answer = 'yes'
    right_answer = 'no'
    return number, right_answer


def is_even_number(number):
    if number % 2:
        return False
    return True
