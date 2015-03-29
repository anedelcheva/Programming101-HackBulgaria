import sys
from random import randint


def generate_numbers():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        n = sys.argv[2]
        text_file = open(filename, "w")
        for i in range(int(n)):
            number = randint(1, 1000)
            text_file.write(str(number) + " ")
        #text_file.write("\n")
        text_file.close()
        '''print (filename)
        print (n)
        text_file.close()
        text_file2 = open(filename, "r")
        text = text_file2.read()
        print (text)
        text_file2.close()'''

if __name__ == '__main__':
    generate_numbers()
