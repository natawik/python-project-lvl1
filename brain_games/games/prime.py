def is_prime(condition):
    if (condition < 2):
        return True
    div = 2
    while(div <= condition / 2):
        if (condition % div == 0):
            return False
        div += 1
    return True


def compare(condition):
    if is_prime(condition):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
