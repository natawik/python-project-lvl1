import prompt
import brain_games.exp_gen
from brain_games.cli import run


def calc():
    name = run()
    exp = brain_games.exp_gen.show_rand_expression()
    question = "Question: {}"
    # Shows a random expression
    wrong_answer = "'{}' is wrong answer ;(. Correct answer was '{}'."
    try_again = "Let's try again, {}!"
    # If the user answered incorrectly.
    correct_answer = "Congratulations, {}!"
    # If all three answers are correct.
    counter = 1
    while(counter <= 3):
        right_answer = brain_games.exp_gen.rand_expression(exp)
        print(question.format(exp))
        answer = prompt.string('Your answer: ')
        if (answer == str(right_answer)):
            print('Correct!')
            exp = brain_games.exp_gen.show_rand_expression()
            counter += 1
        else:
            print(wrong_answer.format(answer, right_answer))
            print(try_again.format(name))
            break
    else:
        print(correct_answer.format(name))
