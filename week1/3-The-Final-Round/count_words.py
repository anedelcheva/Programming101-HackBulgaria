def count_words(arr):
    dict = {}
    for i in range(len(arr)):
        dict[arr[i]] = arr.count(arr[i])
    return dict
