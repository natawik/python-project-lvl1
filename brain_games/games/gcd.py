import prompt
import brain_games.gcd_gen
import brain_games.cli


def find_gcd():
    name = brain_games.cli.run()
    gcd = brain_games.gcd_gen.show_two_rand_numbers()
    counter = 1
    while(counter <= 3):
        right_answer = brain_games.gcd_gen.is_gcd(gcd)
        print(brain_games.cli.question.format(gcd))
        answer = prompt.string('Your answer: ')
        if (answer == str(right_answer)):
            print('Correct!')
            gcd = brain_games.gcd_gen.show_two_rand_numbers()
            counter += 1
        else:
            print(brain_games.cli.wrong_answer.format(answer, right_answer))
            print(brain_games.cli.try_again.format(name))
            break
    else:
        print(brain_games.cli.correct_answer.format(name))
