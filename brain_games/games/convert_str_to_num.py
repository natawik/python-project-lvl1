

def conv_num_1(exp):
    i = 0
    num_1 = ''
    while(exp[i] != ' '):
        num_1 += exp[i]
        i += 1
    return int(num_1)


def conv_num_2(exp):
    i = -1
    num_2 = ''
    while(exp[i] != ' '):
        num_2 += exp[i]
        i -= 1
    num_2 = num_2[::-1]
    return int(num_2)
