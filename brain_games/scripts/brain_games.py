#!/usr/bin/env python3


from brain_games.cli import run


def greet(game=str):
    print('Welcome to the Brain Games!')
    if game == 'even':
        print('Answer "yes" if number even otherwise answer "no".')
    elif game == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'calc':
        print('What is the result of the expression?')
    elif game == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif game == 'progression':
        print('What number is missing in the progression?')


def main():
    greet()


if __name__ == '__main__':
    main()
    run()
