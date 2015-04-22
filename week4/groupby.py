def groupby(func, seq):
    dict = {}
    for item in seq:
        if func(item) not in dict:
            dict[func(item)] = [item]
        else:
            dict[func(item)].append(item)
    return dict
