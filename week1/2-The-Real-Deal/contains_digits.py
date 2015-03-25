def to_digits(n):
    n = abs(n)
    l = []
    while n is not 0:
        l.insert(0, n % 10)
        n = n // 10
    return l


def contains_digits(number, digits):
    digits_to_list = to_digits(number)
    for digit in digits:
        if digit not in digits_to_list:
            return False
    return True
