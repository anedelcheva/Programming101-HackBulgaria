def sum_of_rows(m):
    result = []
    for row in m:
        result.append(sum(row))
    return result
#print (sum_of_rows([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))


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
