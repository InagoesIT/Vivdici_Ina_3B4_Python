# Write a function that receives as a parameter a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match the regular expression.
import re


def get_matches_with_length(regex: str, text: str, length: int) -> list:
    return list(filter(lambda item: len(item) == length, re.findall(regex, text)))


if __name__ == '__main__':
    print(get_matches_with_length(r"\w+", "hey heeeey hy hiii hi", 2))
