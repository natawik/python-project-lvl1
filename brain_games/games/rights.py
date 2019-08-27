import brain_games.games
import brain_games.exp_gen
import brain_games.num_gen
import brain_games.show_rand_num
import brain_games.gcd_gen
import brain_games.progr_gen
import brain_games.prime_gen


def what_is_right(game, condition):
    if game == 'calc':
        right_answer = brain_games.exp_gen.rand_expression(condition)
    elif game == 'even':
        right_answer = brain_games.num_gen.is_even_number(condition)
    elif game == 'prime':
        right_answer = brain_games.prime_gen.compare(condition)
    elif game == 'gcd':
        right_answer = brain_games.gcd_gen.is_gcd(condition)  
    elif game == 'progression':
        right_answer = brain_games.progr_gen.hidden_number(condition)
    return right_answer
