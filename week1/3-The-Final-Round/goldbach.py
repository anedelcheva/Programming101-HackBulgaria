def sum_of_divisors(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0:
            result += i
    return result


def is_prime(n):
    n = abs(n)
    return sum_of_divisors(n) - 1 == n


def goldbach(n):
    current = 2
    result = []
    while current < n:
        if is_prime(current) and is_prime(n - current):
            if (n - current, current) not in result:
                result += [(current, n - current)]
        current += 1
    return result
