def get_nr_of_words(characters):
    nr_of_words = 1
    index = characters.find(' ')

    while index != -1 and index < len(characters) - 1:
        if characters[index + 1] != ' ':
            nr_of_words += 1
        characters = characters[index + 1:]

    return nr_of_words

print(get_nr_of_words("heaaaa a d d"))
