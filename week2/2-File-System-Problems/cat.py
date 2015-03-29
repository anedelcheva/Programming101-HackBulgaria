import sys


def read_file():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        text_file = open(filename, "r")
        text = text_file.read()
        print (text)
        text_file.close()
    else:
        print ("Give me a file to read!")

if __name__ == '__main__':
    read_file()
