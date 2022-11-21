# Write a function that recursively scrolls a directory and displays
# those files whose name matches a regular expression given as a parameter
# or contains a string that matches the same expression.
# Files that satisfy both conditions will be prefixed with ">>"
import os
import re


def file_content_matches(file_path, compiled_expr):
    try:
        file = open(file_path)
        for line in file.readlines():
            if compiled_expr.search(line):
                print("---- matched line: "+line)
                file.close()
                return True
        file.close()
        return False
    except IOError:
        return False


def display_files_that_have(dir_path, expr):
    compiled_expr = re.compile(expr)

    for root, dir_names, file_names in os.walk(dir_path):
        for file_name in file_names:
            is_name_a_match = False
            if compiled_expr.match(file_name):
                is_name_a_match = True

            file_path = os.path.join(root, file_name)
            if file_content_matches(file_path, compiled_expr) is False and not is_name_a_match:
                continue
            print(f"------------------ \033[1m({file_name})\033[0m ----------------")
            print(f"-> File content that matches the regular expression '{expr}':")
            text = ""
            if is_name_a_match:
                text = ">>"
            print(f"{text}{open(file_path).read()}")
            # print(file_name)
            print("=" * 50)


if __name__ == '__main__':
    word_with_3vowels = r"(\w*[aeiou]{3}\w*)"
    variable_assignation = r'[a-zA-Z]\w*\s*=\s*(([a-zA-Z]\w*)|(\d)|("\w*"))'
    display_files_that_have("../lab6", variable_assignation)
