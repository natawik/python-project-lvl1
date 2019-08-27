import brain_games.games
import brain_games.exp_gen
import brain_games.num_gen
import brain_games.show_rand_num
import brain_games.gcd_gen
import brain_games.progr_gen


def game_condition(game):
    if game == 'calc':
        condition = brain_games.exp_gen.show_rand_expression()
    elif ((game == 'even') or (game == 'prime')):
        condition = brain_games.show_rand_num.show_rand_number()
    elif game == 'gcd':
        condition = brain_games.gcd_gen.show_two_rand_numbers()
    elif game == 'progression':
        condition = brain_games.progr_gen.show_progression()
    return condition


def show_condition(condition, right_answer, game):
    if game == 'progression':
        return brain_games.progr_gen.hide_number(condition, right_answer)
    else:
        return condition
