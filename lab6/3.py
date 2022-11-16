# Write a function that receives as a parameter a string of text characters and
# a list of regular expressions and returns a list of strings that match on
# at least one regular expression given as a parameter.
import re


def get_matched_strings(text: str, regexes: list[str]) -> list:
    return re.findall("|".join(regexes), text)


if __name__ == '__main__':
    print(get_matched_strings("call me: 0732342", [r"\d+", r"\w{4}"]))
