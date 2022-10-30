import os
import sys


def get_files_from_directory(dir_path) -> list:
    absolute_path = os.path.abspath(dir_path) + '/'
    all_items_paths = [absolute_path + item for item in os.listdir(absolute_path)]
    return list(filter(lambda item: os.path.isfile(item), all_items_paths))


def main():
    dir_path = "/mnt/uni/COURSES/PYTHON/lab"
    try:
        dir_items = get_files_from_directory(dir_path)
        print(f"All the files from the directory = {dir_path} are:")
        print(dir_items)
    except FileNotFoundError:
        print(f"!!! There is no such directory with the path: --{dir_path}-- !!!")
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
