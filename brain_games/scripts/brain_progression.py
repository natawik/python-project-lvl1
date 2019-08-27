#!/usr/bin/env python3


from brain_games.games.game_engine import engine
from brain_games.scripts.brain_games import main


if __name__ == '__main__':
    main()


print('What number is missing in the progression?')
engine('progression')
