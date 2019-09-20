import prompt
from brain_games import cli


def run(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = cli.greet()
    counter = 1
    while counter <= 3:
        question, right_answer = game.make_round()
        print(cli.QUESTION.format(question))
        answer = prompt.string('Your answer: ')
        if answer != right_answer:
            print(cli.WRONG_ANSWER.format(answer, right_answer))
            print(cli.TRY_AGAIN.format(name))
            break
        print('Correct!')
        counter += 1
    else:
        print(cli.CORRECT_ANSWER.format(name))
