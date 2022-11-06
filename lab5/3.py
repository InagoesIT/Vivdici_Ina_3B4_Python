# Using functions, anonymous functions, list comprehensions and filter, implement three methods to
# generate a list with all the vowels in a given string.
# For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].

def vowels_1(input_string):
    return [character for character in input_string if character in "aeiou"]


def vowels_2(input_string):
    return list(filter(lambda x: x in "aeiou", input_string))


def vowels_3(input_string):
    vowels_indexes = [index for index, char in enumerate(input_string) if char in "aeiou"]
    return [input_string[index] for index in vowels_indexes]


if __name__ == "__main__":
    sentence = "Programming in Python is fun"
    result_vowels_1 = vowels_1(sentence)
    result_vowels_2 = vowels_2(sentence)
    result_vowels_3 = vowels_3(sentence)
    if result_vowels_1.__eq__(result_vowels_2) and result_vowels_1.__eq__(result_vowels_3) and result_vowels_2.__eq__(result_vowels_3):
        print(vowels_3(sentence))
    else:
        print("oops...")
