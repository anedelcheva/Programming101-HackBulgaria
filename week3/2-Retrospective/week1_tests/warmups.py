def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n - 1)


def fibonacci(n):
    fiblist = []
    a = 1
    b = 1
    for i in range(n):
        fiblist.append(a)
        a, b = b, a + b
    return fiblist


def sum_of_digits(n):
    n = abs(n)
    result = 0
    while n is not 0:
        result += n % 10
        n = n // 10
    return result


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


def palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]


def to_number(digits):
    result = 0
    for digit in digits:
        result *= 10
        result += digit
    return result


def fib_number(n):
    return (int("".join(map(str, fibonacci(n)))))


def count_vowels(str):
    str = str.lower()
    counter = 0
    for s in str:
        if s in "aeiouy":
            counter += 1
    return counter


def count_consonants(str):
    str = str.lower()
    counter = 0
    string = "bcdfghjklmnpqrstvwxz"
    for s in str:
        if s in string:
            counter += 1
    return counter


def reverse(element):
    element = str(element)
    element = element[::-1]
    return element


def p_score(n):
    if palindrome(n):
        return 1
    else:
        return 1 + p_score(n + int(reverse(n)))


def char_histogram(string):
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


def is_increasing(seq):
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True


def is_decreasing(seq):
    for i in range(len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            return False
    return True


def count_the_ones(binary):
    counter = 0
    for digit in binary:
        if digit == '1':
            counter += 1
    return counter


def is_hack(n):
    binary = bin(n)
    binary = binary[2:]
    ones = count_the_ones(binary)
    return palindrome(binary) and ones % 2 is not 0


def next_hack(n):
    number = n + 1
    while not is_hack(number):
        number = number + 1
    return number
