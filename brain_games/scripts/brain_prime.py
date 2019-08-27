#!/usr/bin/env python3


from brain_games.games.game_engine import engine


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine('prime')


if __name__ == '__main__':
    main()
