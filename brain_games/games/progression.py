import prompt
from brain_games.progr_gen import hidden_number, hide_number, show_progression
from brain_games.cli import run


def progr():
    name = run()
    progression = show_progression()
    question = "Question: {}"
    # Shows a progression with missing number
    wrong_answer = "'{}' is wrong answer ;(. Correct answer was '{}'."
    try_again = "Let's try again, {}!"
    # If the user answered incorrectly.
    correct_answer = "Congratulations, {}!"
    # If all three answers are correct.
    counter = 1
    while(counter <= 3):
        right_answer = hidden_number(progression)
        print(question.format(hide_number(progression, right_answer)))
        answer = prompt.string('Your answer: ')
        if (answer == str(right_answer)):
            print('Correct!')
            progression = show_progression()
            counter += 1
        else:
            print(wrong_answer.format(answer, right_answer))
            print(try_again.format(name))
            break
    else:
        print(correct_answer.format(name))
