# Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor
# din directorul dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’

import os
import sys


def get_extensions_from_directory(dir_path):
    dir_items = os.listdir(dir_path)
    dir_files = list(filter(lambda item: os.path.isfile(item), dir_items))
    extensions = set(os.path.splitext(file)[1][1:] for file in dir_files)

    return sorted(extensions)


def main():
    dir_path = "/mnt/uni/COURSES/PYTHON/lab/lab4"
    try:
        extensions = get_extensions_from_directory(dir_path)
        print(f"The file extensions from the directory with the path --{dir_path}-- are:")
        print(extensions)
        return 0
    except FileNotFoundError:
        print(f"!!! There is no such directory with the path: --{dir_path}-- !!!")
        return 1


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
