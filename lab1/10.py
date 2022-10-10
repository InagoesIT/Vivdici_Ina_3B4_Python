def get_nr_of_words(characters):
    nr_of_words = 1
    index = characters.find(' ')

    while index != -1:
        if index < len(characters) - 1 and characters[index + 1] != ' ':
            nr_of_words += 1
            characters = characters[index + 1:]
        else:
            while characters.find(' ') != -1:
                characters = characters[1:]
        index = characters.find(' ')

    return nr_of_words

print(get_nr_of_words("heaaaa a d d         g      aa"))
