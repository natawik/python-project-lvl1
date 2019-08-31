import brain_games.games.expression
import brain_games.games.show_rand_num
import brain_games.games.gcd
from brain_games.games.progression import hide_number


def game_condition(game):
    if game == 'calc':
        condition = brain_games.games.expression.show_rand_expression()
    elif ((game == 'even') or (game == 'prime')):
        condition = brain_games.games.show_rand_num.show_rand_number()
    elif game == 'gcd':
        condition = brain_games.games.gcd.show_two_rand_numbers()
    elif game == 'progression':
        condition = brain_games.games.progression.show_progression()
    return condition


def show_cond(condition, right_answer, game):
    if game == 'progression':
        return hide_number(condition, right_answer)
    else:
        return condition
