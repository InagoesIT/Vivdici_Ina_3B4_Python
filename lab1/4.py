def convert_upper_camel_into_snake(characters):
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = characters[0].lower()
    for i in range(1, len(characters)):
        if characters[i] in upper_alphabet:
            result += '_' + characters[i].lower()
            continue
        result += characters[i]

    return result

print(convert_upper_camel_into_snake("HelloCamelCaseHHHH"))
