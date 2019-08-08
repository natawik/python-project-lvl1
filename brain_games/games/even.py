import prompt
import brain_games.num_gen
import brain_games.cli
import brain_games.show_rand_num


def is_even():
    name = brain_games.cli.run()
    number = brain_games.num_gen.show_rand_number()
    # Return a random integer N such that a <= N <= b.
    counter = 1
    while(counter <= 3):
        right_answer = brain_games.num_gen.is_even_number(number)
        print(brain_games.cli.question.format(number))
        answer = prompt.string('Your answer: ')
        if (answer == right_answer):
            print('Correct!')
            number = brain_games.num_gen.show_rand_number()
            counter += 1
        else:
            print(brain_games.cli.wrong_answer.format(answer, right_answer))
            print(brain_games.cli.try_again.format(name))
            break
    else:
        print(brain_games.cli.correct_answer.format(name))
