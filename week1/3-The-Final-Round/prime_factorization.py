def sum_of_divisors(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0:
            result += i
    return result


def is_prime(n):
    n = abs(n)
    return sum_of_divisors(n) - 1 == n


def primes(n):
    primeslist = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primeslist.append(d)
            n //= d
        d += 1
    if n > 1:
        primeslist.append(n)
    return primeslist


def prime_factorization(n):
    dict = count_words(primes(n))
    result = []
    for key in dict:
        result.append((key, dict[key]))
    return result
