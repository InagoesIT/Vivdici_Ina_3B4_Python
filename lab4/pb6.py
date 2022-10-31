# Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior,
# cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru,
# iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu
# instanța excepției ca parametru.

import os.path
import sys

import pb3


def file_has_string(file_path, to_search, callback):
    try:
        file = open(file_path, mode="r")
        if not file.readable():
            file.close()
            return False
        index = file.read().find(to_search)
        file.close()
        return index != -1
    except (IOError, ValueError) as error:
        callback(error)


def get_files_containing_string_from(target, to_search, callback):
    if os.path.isfile(target):
        if file_has_string(target, to_search, callback):
            return [target]
        return []
    elif os.path.isdir(target):
        items_from_dir = pb3.get_all_files_recursively(target)
        files_from_dir = list(filter(lambda item_path: os.path.isfile(item_path), items_from_dir))
        return list(filter(lambda file_path: file_has_string(file_path, to_search, callback), files_from_dir))
    else:
        raise ValueError("!The target isn't a file or a directory!")


def error_handler(error):
    print(f"-> error handler: {error}")


def main():
    dir_path = "/mnt/uni/COURSES/PYTHON/lab/lab4"
    file_path = "/mnt/uni/COURSES/PYTHON/lab/lab4/pb4.py"
    to_search = "sort"
    is_ok = True
    try:
        files = get_files_containing_string_from(dir_path, to_search, error_handler)
        print(f"The files from the directory with the path --{dir_path}-- that contain the string '{to_search}' are:")
        print(files)
        print('-' * 100)
    except ValueError as error:
        print(f"-> !!! There is no such directory with the path: --{dir_path}-- !!!")
        print(f"-> the specific error is: {error}")
        is_ok = False
    try:
        files = get_files_containing_string_from(file_path, to_search, error_handler)
        print(f"The result for the file with the path --{file_path}-- that contain the string '{to_search}' is:")
        print(files)
        return is_ok
    except ValueError as error:
        print(f"-> !!! There is no such file with the path: --{file_path}-- !!!")
        print(f"-> the specific error is: {error}")
        return is_ok


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
