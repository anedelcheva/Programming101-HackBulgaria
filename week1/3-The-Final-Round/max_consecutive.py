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


def max_consecutive(items):
    items = group(items)
    dict = {}
    for i in range(len(items)):
        dict[len(items[i])] = items[i]
    return max(dict)
