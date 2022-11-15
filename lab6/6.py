# Write a function that, for a text given as a parameter, censures words
# that begin and end with vowels. Censorship means replacing characters
# from odd positions with *.

import re


def get_censored_word(word: str) -> str:
    word_list = list(word)
    for i in range(1, len(word), 2):
        word_list[i] = '*'
    return "".join(word_list)


def get_censored_text(text):
    return re.sub(r"(\b[aeiou][a-z]+[aeiou])",
                  lambda intermediary_result: get_censored_word(intermediary_result.group()), text)


if __name__ == '__main__':
    print(get_censored_text("elle ina ionela vasile"))
