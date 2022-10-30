import os
import sys


def get_all_files_recursively(dir_path):
    all_files = list()
    for item in os.listdir(dir_path):
        item_path = f"{dir_path}/{item}"
        if os.path.isdir(item_path):
            all_files += get_all_files_recursively(item_path)
        else:
            all_files.append(item)
    return all_files


def get_extensions_count(files):
    extensions = dict()
    for file in files:
        extension = os.path.splitext(file)[1][1:]
        if extension == "":
            continue

        if extension in extensions:
            extensions[extension] += 1
        else:
            extensions[extension] = 1

    tuple_extensions = [(value, key) for key, value in enumerate(extensions)]
    tuple_extensions.sort(key=lambda tuple_ext: tuple_ext[1], reverse=True)
    return tuple_extensions


def get_characters_or_extensions(my_path):
    if os.path.isfile(my_path):
        file = open(my_path, mode="r")
        return file.read()[-20:]
    elif os.path.isdir(my_path):
        return get_extensions_count(get_all_files_recursively(my_path))
    else:
        raise FileNotFoundError


def main():
    dir_path = "/mnt/uni/COURSES/PYTHON/lab/lab4"
    file_path = "/mnt/uni/COURSES/PYTHON/lab/lab4/result.txt"
    is_ok = True
    try:
        result = get_characters_or_extensions(dir_path)
        print(f"The extensions of the files from the directory with the path --{dir_path}-- are:")
        print(result)
        print('-'*100)
    except FileNotFoundError:
        print(f"!!! There is no such directory with the path: --{dir_path}-- !!!")
        is_ok = False
    try:
        result = get_characters_or_extensions(file_path)
        print(f"The last characters from the file with the path --{file_path}-- are:")
        print(result)
        return is_ok
    except OSError:
        print(f"!!! There is no such file with the path: --{file_path}-- !!!")
        return False


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
