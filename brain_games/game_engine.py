import prompt
import brain_games.conditions
import brain_games.rights
import brain_games.cli
from brain_games.conditions import show_cond
from brain_games.cli import question


def engine(game):
    name = brain_games.cli.run()
    counter = 1
    while(counter <= 3):
        condition = brain_games.conditions.game_condition(game)
        right_answer = brain_games.rights.what_is_right(game, condition)
        print(question.format(show_cond(condition, right_answer, game)))
        answer = prompt.string('Your answer: ')
        if (answer == str(right_answer)):
            print('Correct!')
            condition = brain_games.conditions.game_condition(game)
            counter += 1
        else:
            print(brain_games.cli.wrong_answer.format(answer, right_answer))
            print(brain_games.cli.try_again.format(name))
            break
    else:
        print(brain_games.cli.correct_answer.format(name))
