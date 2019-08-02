import prompt
from brain_games.progr_gen import hidden_number, hide_number, show_progression
import brain_games.cli


def progr():
    name = brain_games.cli.run()
    prog = show_progression()
    counter = 1
    while(counter <= 3):
        right_answer = hidden_number(prog)
        print(brain_games.cli.question.format(hide_number(prog, right_answer)))
        answer = prompt.string('Your answer: ')
        if (answer == str(right_answer)):
            print('Correct!')
            prog = show_progression()
            counter += 1
        else:
            print(brain_games.cli.wrong_answer.format(answer, right_answer))
            print(brain_games.cli.try_again.format(name))
            break
    else:
        print(brain_games.cli.correct_answer.format(name))
