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


def to_digits(n):
    n = abs(n)
    l = []
    while n is not 0:
        l.insert(0, n % 10)
        n = n // 10
    return l


def contains_digit(number, digit):
    digits = to_digits(number)
    # function 'in' checking whether the list digits contains digit
    return digit in digits


def contains_digits(number, digits):
    digits_to_list = to_digits(number)
    for digit in digits:
        if digit not in digits_to_list:
            return False
    return True


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


def count_substrings(haystack, needle):
    return haystack.count(needle)


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


def sum_matrix(m):
    N = len(m)
    M = len(m[0])
    result = 0
    for i in range(N):
        for j in range(M):
            result += m[i][j]
    return result


def neighbours(m):
    N = len(m)
    M = len(m[0])
    dict = {}
    for i in range(N):
        for j in range(M):
            result = []
            i1 = i - 1
            i2 = i + 1
            j1 = j - 1
            j2 = j + 1
            if j in range(1, M - 1) and i in range(1, N - 1):
                result.append(m[i1][j1])
                result.append(m[i1][j])
                result.append(m[i1][j2])
                result.append(m[i][j1])
                result.append(m[i][j2])
                result.append(m[i2][j1])
                result.append(m[i2][j])
                result.append(m[i2][j2])
                dict[(i, j)] = result
            elif i in range(1, N - 1) and j == 0:
                result.append(m[i1][j2])
                result.append(m[i1][j])
                result.append(m[i][j2])
                result.append(m[i2][j])
                result.append(m[i2][j2])
                dict[(i, j)] = result
            elif i in range(1, N - 1) and j == M - 1:
                result.append(m[i1][j])
                result.append(m[i1][j1])
                result.append(m[i2][j1])
                result.append(m[i][j1])
                result.append(m[i2][j])
                dict[(i, j)] = result
            elif i == 0 and j in range(1, M - 1):
                result.append(m[i][j1])
                result.append(m[i2][j1])
                result.append(m[i2][j])
                result.append(m[i2][j2])
                result.append(m[i][j2])
                dict[(i, j)] = result
            elif i == N - 1 and j in range(1, M - 1):
                result.append(m[i1][j1])
                result.append(m[i1][j])
                result.append(m[i1][j2])
                result.append(m[i][j1])
                result.append(m[i][j2])
                dict[(i, j)] = result
            elif i == 0 and j == 0:
                result.append(m[i][j2])
                result.append(m[i2][j2])
                result.append(m[i2][j])
                dict[(i, j)] = result
            elif i == 0 and j == M - 1:
                result.append(m[i][j1])
                result.append(m[i2][j1])
                result.append(m[i2][j])
                dict[(i, j)] = result
            elif i == N - 1 and j == 0:
                result.append(m[i1][j])
                result.append(m[i1][j2])
                result.append(m[i][j2])
                dict[(i, j)] = result
            elif i == N - 1 and j == M - 1:
                result.append(m[i][j1])
                result.append(m[i1][j1])
                result.append(m[i1][j])
                dict[(i, j)] = result
    return dict


def before_bombing(m):
    dict = neighbours(m)
    for key in dict:
        dict[key] = sum(dict[key])
    return dict


def after_bombing(m):
    dict = neighbours(m)
    for key in dict:
        target = m[key[0]][key[1]]
        for i in range(len(dict[key])):
            if dict[key][i] - target < 0:
                dict[key][i] = 0
            else:
                dict[key][i] -= target
    for key in dict:
        dict[key] = sum(dict[key])
    return dict


def matrix_bombing_plan(m):
    dict1 = before_bombing(m)
    dict2 = after_bombing(m)
    s = sum_matrix(m)
    for key in dict1:
        dict1[key] -= dict2[key]
        dict1[key] = s - dict1[key]
    return dict1
