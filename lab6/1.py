# Write a function that extracts the words from a given text as a parameter.
# A word is defined as a sequence of alphanumeric characters.

import re


def get_words(text: str) -> list:
    return re.findall(r"(?!_)\w+", text)


if __name__ == '__main__':
    print(get_words("Hello, my name is Hellen. My number _is: 111."))
