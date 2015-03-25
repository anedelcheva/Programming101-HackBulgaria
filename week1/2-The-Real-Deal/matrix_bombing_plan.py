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
