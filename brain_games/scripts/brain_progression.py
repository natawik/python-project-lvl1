#!/usr/bin/env python3


from brain_games.games.game_engine import engine


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    engine('progression')


if __name__ == '__main__':
    main()
