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
        print(f"The file extensions from the directory with the path --{sys.argv[1]}-- are:")
        print(get_extensions_from_dir_with_args())
        return 0
    except FileNotFoundError:
        print(f"!!! There is no such directory with the path: --{sys.argv[1]}-- !!!")
        return 1


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
