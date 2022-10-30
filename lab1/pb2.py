def get_nr_of_vowels(characters):
    nr_of_vowels = 0
    characters = characters.lower()

    for char in characters:
        if char in ["a", "e", "i", "o", "u"]:
            nr_of_vowels += 1

    return nr_of_vowels


print(get_nr_of_vowels("eu sunt eu, tu esti tu"))
print(get_nr_of_vowels("brouhaha"))
print(get_nr_of_vowels("pftpft"))
