# Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

def clear_duplicates(numbers):
    duplicates = list()
    cleared_list = list(numbers)
    i, j = 0, 0

    while i < len(cleared_list):
        while j < len(cleared_list):
            if i != j and cleared_list[i] == cleared_list[j]:
                duplicates.append(cleared_list[i])
                cleared_list.pop(j)
            else:
                j += 1
        i += 1
        j = 0

    return duplicates, cleared_list


def remove_from(a, b):
    cleared_list = list(a)

    for element in b:
        cleared_list.remove(element)

    return cleared_list


def get_intersection_union_difference(a: list, b: list) -> tuple[list, list, list, list]:
    merged_list = a + b
    intersection, union = clear_duplicates(merged_list)
    difference_a_b = remove_from(a, intersection)
    difference_b_a = remove_from(b, intersection)

    return intersection, union, difference_a_b, difference_b_a


if __name__ == '__main__':
    print(get_intersection_union_difference([1, 2, 3, 4, 5], [1, 3, 5, 7, 9]))
