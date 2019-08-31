#!/usr/bin/env python3


from brain_games.games.game_engine import engine
from brain_games.scripts.brain_games import greet


def main():
    greet()
    print('Answer "yes" if number even otherwise answer "no".')
    engine('even')


if __name__ == '__main__':
    main()
