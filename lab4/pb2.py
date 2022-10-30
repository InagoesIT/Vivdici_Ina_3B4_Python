import os
import sys

import pb8


def write_to_file_items_from_dir(dir_path, file_path):
    file = open(file_path, mode='w')
    file_name_index = len(dir_path)
    dir_items = list(filter(lambda item: item[file_name_index] == 'A', pb8.get_files_from_directory(dir_path)))
    for dir_item in dir_items:
        file.write(dir_item)


def main():
    dir_path = "/mnt/uni/COURSES/PYTHON/lab/lab4/"
    file_path = "/mnt/uni/COURSES/PYTHON/lab/lab4/result.txt"
    try:
        write_to_file_items_from_dir(dir_path, file_path)
        return 0
    except FileNotFoundError:
        print(f"!!! There is no such directory with the path: --{dir_path}-- !!!")
        return 1
    except OSError:
        print(f"!!! There is no such file with the path: --{file_path}-- !!!")
        return 1


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit

