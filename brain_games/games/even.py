import prompt
import brain_games.num_gen
from brain_games.cli import run


def is_even():
    name = run()
    number = brain_games.num_gen.show_rand_number()
    # Return a random integer N such that a <= N <= b.
    question = "Question: {}"
    # Shows a random number
    wrong_answer = "'{}' is wrong answer ;(. Correct answer was '{}'."
    try_again = "Let's try again, {}!"
    # If the user answered incorrectly.
    correct_answer = "Congratulations, {}!"
    # If all three answers are correct.
    counter = 1
    while(counter <= 3):
        print(question.format(number))
        answer = prompt.string('Your answer: ')
        right_answer = brain_games.num_gen.is_even_number(number)
        if (answer == right_answer):
            print('Correct!')
            number = brain_games.num_gen.show_rand_number()
            counter += 1
        else:
            print(wrong_answer.format(answer, right_answer))
            print(try_again.format(name))
            break
    else:
        print(correct_answer.format(name))
