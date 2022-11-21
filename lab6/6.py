# Write a function that, for a text given as a parameter, censures words
# that begin and end with vowels. Censorship means replacing characters
# from odd positions with *.

import re


def get_censored_text(text: str) -> str:
    return re.sub(r"(\b[aeiou][a-z]*[aeiou])",
                  lambda intermediary_result: re.sub(r"([a-z])[a-z]", r"\1*", intermediary_result.group(),
                                                     flags=re.IGNORECASE), text)


if __name__ == '__main__':
    print(get_censored_text("elle ina ionela vasile"))
