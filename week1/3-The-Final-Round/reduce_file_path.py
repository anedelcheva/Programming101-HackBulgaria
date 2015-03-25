def reduce_file_path(path):
    path = path.split('/')
    path = [item for item in path if item != '' and item != '.']
    if path == []:
        return "/"
    new = []
    length = len(path)
    for i in range(length - 1):
        if path[i + 1] != '..':
            new.append(path[i])
    new.append(path[length - 1])
    new = [item for item in new if item != '..']
    new = '/' + '/'.join(new)
    return new
