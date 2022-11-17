# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
import math


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_primes_from(numbers: list) -> list:
    return list(filter(lambda number: is_prime(number), numbers))


if __name__ == '__main__':
    print(get_primes_from([i for i in range(25)]))
