# Write a function that receives a variable number of arguments and keyword arguments.
# The function returns a list containing only the arguments which are dictionaries,
# containing minimum 2 keys and at least one string key with minimum 3 characters.
# Example:
# my_function(
#  {1: 2, 3: 4, 5: 6},
#  {'a': 5, 'b': 7, 'c': 'e'},
#  {2: 3},
#  [1, 2, 3],
#  {'abc': 4, 'def': 5},
#  3764,
#  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#  test={1: 1, 'test': True}
# ) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]


def get_dicts_with_conditions(*args, **dictionaries):
    result_dictionaries = []
    bag_of_arguments = [args, dictionaries.values()]

    for args_arr in bag_of_arguments:
        for arg in args_arr:
            if type(arg) == dict and len(arg.keys()) >= 2 and \
                    any([True if type(key) == str and len(key) > 2 else False for key in arg.keys()]):
                result_dictionaries.append(arg)
    return result_dictionaries


if __name__ == '__main__':
    print(get_dicts_with_conditions({1: 2, 3: 4, 5: 6},
                                    {'a': 5, 'b': 7, 'c': 'e'},
                                    {2: 3},
                                    [1, 2, 3],
                                    {'abc': 4, 'def': 5},
                                    3764,
                                    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                                    test={1: 1, 'test': True}))
