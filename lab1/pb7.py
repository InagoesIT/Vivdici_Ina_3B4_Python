def find_number_in_string(characters):
    digits = '0123456789'
    start_index = -1

    for digit in digits:
        start_index = characters.find(digit)
        if start_index != -1:
            break

    if start_index == -1:
        return None

    i = start_index + 1
    while characters[i] in digits:
        i += 1

    return characters[start_index:i]


print(find_number_in_string("An apple is 123 USD"))
print(find_number_in_string("abc556abc"))
