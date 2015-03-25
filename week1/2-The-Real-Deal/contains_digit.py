def to_digits(n):
    n = abs(n)
    l = []
    while n is not 0:
        l.insert(0, n % 10)
        n = n // 10
    return l


def contains_digit(number, digit):
    digits = to_digits(number)
    return digit in digits
