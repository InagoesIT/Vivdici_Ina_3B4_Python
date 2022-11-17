# Write a function to return a list of the first n numbers in the Fibonacci string.

def first_n_fibonacci(n: int) -> list:
    fibonacci_list = [0, 1]
    if n == 1:
        return [fibonacci_list[0]]

    for i in range(2, n-1):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])

    return fibonacci_list


if __name__ == '__main__':
    print(first_n_fibonacci(5))
    print(first_n_fibonacci(1))
    print(first_n_fibonacci(2))
    print(first_n_fibonacci(15))
