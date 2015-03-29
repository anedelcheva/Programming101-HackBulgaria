import sys
import os
from os.path import join


def find_size_directory():
    if len(sys.argv) == 2:
        try:
            dir_path = sys.argv[1]
            result = 0
            for dirs, subdirs, files in os.walk(dir_path):
                for file in files:
                    path = join(dirs, file)
                    result += os.stat(path).st_size
            return result / (1024 * 1024)
        except OSError as error:
            print (error)
    else:
        print ("No directory")

if __name__ == '__main__':
    print (find_size_directory())
