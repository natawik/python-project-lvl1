#!/usr/bin/env python3


from brain_games.games.game_engine import engine


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    engine('even')


if __name__ == '__main__':
    main()
