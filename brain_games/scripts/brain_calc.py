#!/usr/bin/env python3


from brain_games.games.game_engine import engine
from brain_games.scripts.brain_games import greet


def main():
    greet()
    print('What is the result of the expression?')
    engine('calc')


if __name__ == '__main__':
    main()
