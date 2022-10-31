# Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul
# dat ca argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală.

import os

import sys


def get_extensions_from_dir_with_args():
    dir_path = sys.argv[1]
    dir_items = os.listdir(dir_path)
    extensions = set(os.path.splitext(item)[1][1:] for item in dir_items)
    extensions.remove('')

    return sorted(extensions)


def main():
    try:
        extensions = get_extensions_from_dir_with_args()
        print(f"The file extensions from the directory with the path --{sys.argv[1]}-- are:")
        print(extensions)
        return 0
    except FileNotFoundError:
        print(f"!!! There is no such directory with the path: --{sys.argv[1]}-- !!!")
        return 1


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
