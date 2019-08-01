import prompt
import brain_games.gcd_gen
from brain_games.cli import run


def find_gcd():
    name = run()
    gcd = brain_games.gcd_gen.show_two_rand_numbers()
    question = "Question: {}"
    # Shows a two random number
    wrong_answer = "'{}' is wrong answer ;(. Correct answer was '{}'."
    try_again = "Let's try again, {}!"
    # If the user answered incorrectly.
    correct_answer = "Congratulations, {}!"
    # If all three answers are correct.
    counter = 1
    while(counter <= 3):
        right_answer = brain_games.gcd_gen.is_gcd(gcd)
        print(question.format(gcd))
        answer = prompt.string('Your answer: ')
        if (answer == str(right_answer)):
            print('Correct!')
            gcd = brain_games.gcd_gen.show_two_rand_numbers()
            counter += 1
        else:
            print(wrong_answer.format(answer, right_answer))
            print(try_again.format(name))
            break
    else:
        print(correct_answer.format(name))
