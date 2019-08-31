from random import randint
import brain_games.games.convert_str_to_num


def show_two_rand_numbers():
    exp_gen = (randint(1, 100), randint(1, 100))
    (num_1, num_2) = exp_gen
    show = '{} {}'
    return (show.format(num_1, num_2))


def is_gcd(gcd):
    num_1 = brain_games.games.convert_str_to_num.conv_num_1(gcd)
    num_2 = brain_games.games.convert_str_to_num.conv_num_2(gcd)
    while(num_1 != num_2):
        if(num_1 > num_2):
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return num_1
