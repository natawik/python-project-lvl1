import brain_games.games.prime
import brain_games.games.expression
import brain_games.games.number
import brain_games.games.show_rand_num
import brain_games.games.gcd
import brain_games.games.progression


def what_is_right(game, condition):
    if game == 'calc':
        right_answer = brain_games.games.expression.rand_expression(condition)
    elif game == 'even':
        right_answer = brain_games.games.number.is_even_number(condition)
    elif game == 'prime':
        right_answer = brain_games.games.prime.compare(condition)
    elif game == 'gcd':
        right_answer = brain_games.games.gcd.is_gcd(condition)
    elif game == 'progression':
        right_answer = brain_games.games.progression.hidden_number(condition)
    return right_answer
