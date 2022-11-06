# Create a function and an anonymous function that receive a variable number of arguments.
# Both will return the sum of the values of the keyword arguments.
# Example:
# For the call my_function(1, 2, c=3, d=4) the returned value will be 7.


anonymous_function: () = lambda *args, **dictionary: sum(dictionary.values())


def my_function(*args, **dictionary):
    return sum(dictionary.values())
