def to_digits(n):
    n = abs(n)
    l = []
    while n is not 0:
        l.insert(0, n % 10)
        n = n // 10
    return l


def to_number(digits):
    result = 0
    for digit in digits:
        result *= 10
        result += digit
    return result


def zero_insert(n):
    list = to_digits(n)
    result = []
    for i in range(len(list) - 1):
        result.append(list[i])
        if list[i] == list[i + 1] or (list[i] + list[i + 1]) % 10 == 0:
            result.append(0)
    result.append(list[len(list) - 1])
    return to_number(result)
