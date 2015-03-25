def to_digits(n):
    n = abs(n)
    l = []
    while n is not 0:
        l.insert(0, n % 10)
        n = n // 10
    return l


def is_credit_card_valid(number):
    to_list = to_digits(number)
    digits = []
    new = []
    if len(to_list) % 2 == 0:
        return False
    for i in range(len(to_list)):
        if i % 2 != 0:
            to_list[i] *= 2
    for i in range(len(to_list)):
        if to_list[i] > 9:
            digits = to_digits(to_list[i])
            new += digits
        else:
            new += [to_list[i]]
    return sum(new) % 10 == 0
