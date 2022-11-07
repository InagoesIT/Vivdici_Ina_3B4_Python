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


def has_str_key_min_3_chars(keys):
    return any([True if type(key) == str and len(key) > 2 else False for key in keys])


def condition_is_met(arg):
    return type(arg) == dict and len(arg.keys()) >= 2 and has_str_key_min_3_chars(arg.keys())


def get_dicts_with_conditions(*args, **keyword_args):
    result_dictionaries = []
    bag_of_arguments = [args, keyword_args.values()]

    for args_list in bag_of_arguments:
        for arg in args_list:
            if condition_is_met(arg):
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
