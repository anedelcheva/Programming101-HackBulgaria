def count_words(arr):
    dict = {}
    for i in range(len(arr)):
        dict[arr[i]] = arr.count(arr[i])
    return dict


def unique_words_count(arr):
    arr = set(arr)
    arr = list(arr)
    return len(arr)


def nan_expand(times):
    if times == 0:
        return ""
    nan = times * "Not a "
    result = nan + "NaN"
    return result


def iterations_of_nan_expand(expanded):
    expanded = expanded.split()
    if len(expanded) == 0:
        return 0
    if expanded[len(expanded) - 1] != "NaN":
        return False
    for i in range(len(expanded) - 1):
        if i % 2 == 0 and expanded[i] != "Not":
            return False
        elif i % 2 != 0 and expanded[i] != "a":
            return False
    return len(expanded) // 2
    print (expanded)


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
    result = sorted(result, key=lambda pair: pair[0])
    return result


def group(list):
    sublist = []
    counter = 1
    result = []
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            counter += 1
        else:
            sublist = counter * [list[i]]
            result.append(sublist)
            sublist = []
            counter = 1
    result.append([list[len(list) - 1]] * counter)
    return result


def groupby(func, seq):
    dict = {}
    for item in seq:
        if func(item) not in dict:
            dict[func(item)] = [item]
        else:
            dict[func(item)].append(item)
    return dict


def max_consecutive(items):
    items = group(items)
    dict = {}
    for i in range(len(items)):
        dict[len(items[i])] = items[i]
    return max(dict)


def prepare_meal(number):
    n = 1
    counter = 0
    spam = ''
    eggs = ''
    result = []
    while number >= (3 ** n):
        if number % (3 ** n) == 0:
            counter = n
            result.append("spam")
        n += 1
    if counter == 0:
        result = []
    spam = " ".join(result)
    if spam == '' and number % 5 == 0:
        eggs = 'eggs'
    elif spam != '' and number % 5 == 0:
        eggs = ' and eggs'
    return spam + eggs


def reduce_file_path(path):
    path = path.split('/')
    path = [item for item in path if item != '' and item != '.']
    if path == []:
        return "/"
    new = []
    length = len(path)
    for i in range(length - 1):
        if path[i + 1] != '..':
            new.append(path[i])
    new.append(path[length - 1])
    new = [item for item in new if item != '..']
    new = '/' + '/'.join(new)
    return new


def is_an_bn(word):
    if word == "":
        return True
    word = group(word)
    return len(word) == 2 and len(word[0]) == len(word[1]) \
        and word[0][0] == 'a' and word[1][0] == 'b'


def to_digits(n):
    n = abs(n)
    l = []
    while n is not 0:
        l.insert(0, n % 10)
        n = n // 10
    return l


def is_credit_card_valid(number):
    to_list = to_digits(number)
    digits = []
    new = []
    if len(to_list) % 2 == 0:
        return False
    for i in range(len(to_list)):
        if i % 2 != 0:
            to_list[i] *= 2
    for i in range(len(to_list)):
        if to_list[i] > 9:
            digits = to_digits(to_list[i])
            new += digits
        else:
            new += [to_list[i]]
    return sum(new) % 10 == 0


def goldbach(n):
    current = 2
    result = []
    while current < n:
        if is_prime(current) and is_prime(n - current):
            if (n - current, current) not in result:
                result += [(current, n - current)]
        current += 1
    return result


def sum_of_rows(m):
    result = []
    for row in m:
        result.append(sum(row))
    return result


def sum_of_columns(m):
    columns = []
    for i in range(len(m)):
        column = []
        for j in range(len(m)):
            column += [m[j][i]]
        columns.append(column)
    result = []
    for column in m:
        result.append(sum(column))
    return result


def sum_main_diagonal(m):
    result = 0
    for i in range(len(m)):
        result += m[i][i]
    return result


def sum_secondary_diagonal(m):
    result = 0
    for i in range(len(m)):
        for j in range(len(m)):
            if i + j == len(m) - 1:
                result += m[i][j]
    return result


def all(list):
    for i in range(len(list) - 1):
        if list[i] != list[i + 1]:
            return False
    return True


def sum_rows_columns_diagonals(m):
    result = sum_of_columns(
        m) + sum_of_rows(m) + [sum_main_diagonal(m)] + [sum_secondary_diagonal(m)]
    return result


def magic_square(m):
    return all(sum_rows_columns_diagonals(m))


def is_year_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


import calendar


def friday_years(start, end):
    counter = 0
    while start <= end:
        if calendar.isleap(start) and \
            (calendar.weekday(start, 1, 1) == 4 or
             calendar.weekday(start, 1, 2) == 4):
            counter += 1
        elif calendar.weekday(start, 1, 1) == 4:
            counter += 1
        start += 1
    return counter
