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


def is_an_bn(word):
    if word == "":
        return True
    word = group(word)
    return len(word) == 2 and len(word[0]) == len(word[1]) \
        and word[0][0] == 'a' and word[1][0] == 'b'
