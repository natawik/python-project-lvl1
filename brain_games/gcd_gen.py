from random import randint


def show_two_rand_numbers():
    exp_gen = (randint(1, 100), randint(1, 100))
    (num_1, num_2) = exp_gen
    show = '{} {}'
    return (show.format(num_1, num_2))


def conv_num_1(gcd):
    i = 0
    num_1 = ''
    while(gcd[i] != ' '):
        num_1 += gcd[i]
        i += 1
    return int(num_1)


def conv_num_2(gcd):
    i = -1
    num_2 = ''
    while(gcd[i] != ' '):
        num_2 += gcd[i]
        i -= 1
    num_2 = num_2[::-1]
    return int(num_2)


def is_gcd(gcd):
    num_1 = conv_num_1(gcd)
    num_2 = conv_num_2(gcd)
    while(num_1 != num_2):
        if(num_1 > num_2):
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return num_1
