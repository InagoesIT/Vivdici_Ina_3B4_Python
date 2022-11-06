# Write a module named utils.py that contains one function called process_item.
# The function will have one parameter, x, and will return the least prime number greater than x.
# When run, the module will request an input from the user, convert it to a number, and it will display
# the output of the process_item function.

def process_item(x):
    nr = x + 1

    while True:
        is_prime = True
        for i in range(2, nr//2 + 1):
            if (nr % i) == 0:
                is_prime = False
                break
        if is_prime:
            return nr
        nr += 1


def main():
    x = int(input("Please give a number => "))
    print(f"The output for process_item({x}) = {process_item(x)}")


if __name__ == "__main__":
    main()
