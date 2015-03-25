def nan_expand(times):
    if times == 0:
        return ""
    nan = times * "Not a "
    result = nan + "NaN"
    return result
