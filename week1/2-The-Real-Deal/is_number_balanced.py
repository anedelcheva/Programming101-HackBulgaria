def to_digits(n):
    n = abs(n)
    l = []
    while n is not 0:
        l.insert(0, n % 10)
        n = n // 10
    return l


def is_even(list):
    return len(list) % 2 == 0


def is_number_balanced(n):
    digits_to_list = to_digits(n)
    middle = len(digits_to_list) // 2
    first = digits_to_list[0: middle]
    if is_even(digits_to_list):
        last = digits_to_list[middle: len(digits_to_list)]
        return sum(first) == sum(last)
    else:
        last = digits_to_list[middle + 1: len(digits_to_list)]
        return sum(first) == sum(last)
