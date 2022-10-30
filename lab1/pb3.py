def get_occurrences(string1, string2):
    nr_of_occurrences = 0
    string2_size = len(string2)

    while len(string1) > string2_size:
        i = string1.find(string2)
        if i != -1:
            nr_of_occurrences += 1
            string1 = string1[(i + string2_size) - 1:]

    return nr_of_occurrences


print(get_occurrences("eueueueueue", "eu"))
