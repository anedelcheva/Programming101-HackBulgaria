def sum_of_divisors(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0:
            result += i
    return result


def is_prime(n):
    n = abs(n)
    return sum_of_divisors(n) - 1 == n


def number_of_divisors(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return counter


def prime_number_of_divisors(n):
    return is_prime(number_of_divisors(n))
