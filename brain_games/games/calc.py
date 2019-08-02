import prompt
import brain_games.exp_gen
import brain_games.cli


def calc():
    exp = brain_games.exp_gen.show_rand_expression()
    counter = 1
    while(counter <= 3):
        right_answer = brain_games.exp_gen.rand_expression(exp)
        print(brain_games.cli.question.format(exp))
        answer = prompt.string('Your answer: ')
        if (answer == str(right_answer)):
            print('Correct!')
            exp = brain_games.exp_gen.show_rand_expression()
            counter += 1
        else:
            print(brain_games.cli.wrong_answer.format(answer, right_answer))
            print(brain_games.cli.try_again.format(brain_games.cli.name))
            break
    else:
        print(brain_games.cli.correct_answer.format(brain_games.cli.name))
