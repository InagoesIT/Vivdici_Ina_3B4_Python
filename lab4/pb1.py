import os
import sys


def get_extensions_from_directory(dir_path):
    dir_items = os.listdir(dir_path)
    extensions = set(os.path.splitext(item)[1][1:] for item in dir_items)
    extensions.remove('')

    return sorted(extensions)


def main():
    dir_path = "/mnt/uni/COURSES/PYTHON/lab/lab4"
    try:
        print(f"The file extensions from the directory with the path --{dir_path}-- are:")
        print(get_extensions_from_directory(dir_path))
        return 0
    except FileNotFoundError:
        print(f"!!! There is no such directory with the path: --{dir_path}-- !!!")
        return 1


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
