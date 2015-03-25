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
