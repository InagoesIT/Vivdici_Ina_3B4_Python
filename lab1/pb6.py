def is_palindrome(number):
    str_number = str(number)
    last_index = len(str_number) - 1

    for i in range((last_index + 1) // 2):
        if str_number[i] != str_number[last_index]:
            return False
        last_index -= 1

    return True

print(is_palindrome(112311))
