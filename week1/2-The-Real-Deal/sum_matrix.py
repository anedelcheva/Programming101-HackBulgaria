def sum_matrix(m):
    N = len(m)
    M = len(m[0])
    result = 0
    for i in range(N):
        for j in range(M):
            result += m[i][j]
    return result
