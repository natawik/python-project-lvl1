import prompt
import brain_games.cli


def run(game):
    name = brain_games.cli.greet()
    counter = 1
    while counter <= 3:
        condition, right_answer = game
        print(brain_games.cli.QUESTION.format(condition))
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            counter += 1
        else:
            print(brain_games.cli.WRONG_ANSWER.format(answer, right_answer))
            print(brain_games.cli.TRY_AGAIN.format(name))
            break
    else:
        print(brain_games.cli.CORRECT_ANSWER.format(name))
