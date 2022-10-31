# Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și
# returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier,
# se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele
# din acel director. Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError
# cu un mesaj corespunzator.

import os.path
import sys
from pb3 import get_all_files_recursively


def file_has_string(file_path, to_search):
    try:
        file = open(file_path, mode="r")
        if not file.readable():
            file.close()
            return False
        index = file.read().find(to_search)
        file.close()
        return index != -1
    except IOError:
        return False
    except ValueError:
        return False


def get_files_containing_string_from(target, to_search):
    if os.path.isfile(target):
        if file_has_string(target, to_search):
            return [target]
        return []
    elif os.path.isdir(target):
        items_from_dir = get_all_files_recursively(target)
        files_from_dir = list(filter(lambda item_path: os.path.isfile(item_path), items_from_dir))
        return list(filter(lambda file_path: file_has_string(file_path, to_search), files_from_dir))
    else:
        raise ValueError("!The target isn't a file or a directory!")


def main():
    dir_path = "/mnt/uni/COURSES/PYTHON/lab/lab4"
    file_path = "/mnt/uni/COURSES/PYTHON/lab/lab4/pb4.py"
    to_search = "sort"
    is_ok = True
    try:
        files = get_files_containing_string_from(dir_path, to_search)
        print(f"The files from the directory with the path --{dir_path}-- that contain the string '{to_search}' are:")
        print(files)
        print('-'*100)
    except ValueError:
        print(f"!!! There is no such directory with the path: --{dir_path}-- !!!")
        print(str(ValueError))
        is_ok = False
    try:
        files = get_files_containing_string_from(file_path, to_search)
        print(f"The result for the file with the path --{file_path}-- that contain the string '{to_search}' is:")
        print(files)
        return is_ok
    except ValueError:
        print(f"!!! There is no such file with the path: --{file_path}-- !!!")
        print(str(ValueError))
        return is_ok


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
