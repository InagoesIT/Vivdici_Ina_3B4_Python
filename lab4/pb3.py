# Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere
# din conținutul fișierului. Dacă parametrul reprezintă calea către un director, se va returna o
# listă de tuple (extensie, count), sortată descrescător după count, unde extensie reprezintă
# extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate
# fișierele (recursiv) din directorul dat ca parametru.

import os
import sys


def get_all_files_recursively(dir_path):
    all_files = list()
    for item in os.listdir(dir_path):
        item_path = f"{dir_path}/{item}"
        if os.path.isdir(item_path):
            all_files += get_all_files_recursively(item_path)
        else:
            all_files.append(item_path)
    return all_files


def get_extensions_count(files):
    extensions = [os.path.splitext(file)[1][1:] for file in files]
    extensions_set = set(extensions)
    extensions_set.remove('')
    tuple_extensions = [(extension, extensions.count(extension)) for extension in extensions_set]
    tuple_extensions.sort(key=lambda tuple_ext: tuple_ext[1], reverse=True)
    return tuple_extensions


def get_characters_or_extensions(my_path):
    if os.path.isfile(my_path):
        file = open(my_path, mode="r")
        characters = file.read()[-20:]
        file.close()
        return characters
    elif os.path.isdir(my_path):
        return get_extensions_count(get_all_files_recursively(my_path))
    else:
        raise FileNotFoundError


def main():
    dir_path = "/mnt/uni/COURSES/PYTHON/"
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
