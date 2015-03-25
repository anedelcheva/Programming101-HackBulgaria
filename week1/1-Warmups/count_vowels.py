def count_vowels(str):
    str = str.lower()
    counter = 0
    for s in str:
        if s in "aeiouy":
            counter += 1
    return counter
