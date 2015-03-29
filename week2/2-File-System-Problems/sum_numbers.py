def find_sum_of_numbers_in_string(string):
    string = string.split()
    for i in range(len(string)):
        string[i] = int(string[i])
    return sum(string)


import sys


def sum_numbers():
    result = 0
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file_object = open(filename, 'r')
        string = file_object.readline()
        sum_of_a_line = find_sum_of_numbers_in_string(string)
        result += sum_of_a_line
    return result

if __name__ == '__main__':
    print(sum_numbers())
