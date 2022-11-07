# Write a function called print_arguments with one parameter named function.
# The function will return one new function which prints the arguments and the
# keyword arguments received and will return the output of the function receives as a parameter.
# Example:
# def multiply_by_two(x):
#     return x * 2
# def add_numbers(a, b):
#     return a + b
# augmented_multiply_by_two = print_arguments(multiply_by_two)
# x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
# augmented_add_numbers = print_arguments(add_numbers)
# x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.

def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def new_function(*args, **kwargs):
        print(f"Arguments are: {args}, {kwargs}")
        return function(*args, *kwargs)

    return new_function


if __name__ == '__main__':
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
    # print(x)
    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
    # print(x)
