def palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]


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
