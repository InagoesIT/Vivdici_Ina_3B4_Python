# Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă
# calea către un fișer si returnează un dicționar cu următoarele cămpuri: full_path =
# calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca se poate
# citi din/scrie in fisier.

import os.path
import sys


def get_file_path_info(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("NOT A FILE!")
    info_dict = dict()
    info_dict["full_path"] = os.path.abspath(file_path)
    info_dict["file_size"] = os.path.getsize(file_path)
    info_dict["file_extension"] = os.path.splitext(file_path)[1][1:]
    file = open(file_path, mode="r")
    info_dict["can_read"] = file.readable()
    file.close()
    file = open(file_path, mode="a")
    info_dict["can_write"] = file.writable()
    file.close()

    return info_dict


def main():
    file_path = "/mnt/uni/COURSES/PYTHON/lab/lab4/pb1.py"
    try:
        file_info = get_file_path_info(file_path)
        print(f"The information about the file with the path = {file_path} is:")
        print(file_info)
    except FileNotFoundError as exception:
        print(exception)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
