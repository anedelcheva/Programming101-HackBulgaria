import sys


def main():
    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        text_file = open(filename, "r")
        text = text_file.read()
        print (text)
        text_file.close()

if __name__ == '__main__':
    main()
