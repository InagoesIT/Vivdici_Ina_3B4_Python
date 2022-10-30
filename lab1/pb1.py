def get_gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1


def get_numbers_from_console():
    numbers = input("Please enter your numbers.")
    numbers = numbers.split(" ")

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    return numbers


def get_gcd_for_array():
    numbers = get_numbers_from_console()
    num1 = numbers[0]
    num2 = numbers[1]

    gcd = get_gcd(num1, num2)
    for i in range(2, len(numbers)):
        gcd = get_gcd(gcd, numbers[i])

    return gcd


print("The greatest common divisor is:", get_gcd_for_array())
