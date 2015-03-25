def to_digits(n):
    n = abs(n)
    l = []
    while n is not 0:
        l.insert(0, n % 10)
        n = n // 10
    return l


def fact_digits(n):
    list = to_digits(n)
    result = []
    for number in list:
        result.append(factorial(number))
    return sum(result)
