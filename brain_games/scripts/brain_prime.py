#!/usr/bin/env python3


from brain_games.games.game_engine import engine
from brain_games.scripts.brain_games import greet


def main():
    greet()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine('prime')


if __name__ == '__main__':
    main()
