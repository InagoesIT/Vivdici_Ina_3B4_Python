# Write a function with one parameter which represents a list.
# The function will return a new list containing all the numbers found in the given list.
# Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]

def get_numbers(input_list):
    return list(filter(lambda x: type(x) == int or type(x) == float, input_list))


if __name__ == '__main__':
    print(get_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
