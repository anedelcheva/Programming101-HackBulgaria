def count_consonants(str):
    str = str.lower()
    counter = 0
    for s in str:
        if s in "bcdfghjklmnpqrstvwxz":
            counter += 1
    return counter
