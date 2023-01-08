initial_str = input()


def palindrome_check(string: str) -> bool:
    new_string = ''

    for char in string:
        if char.isalpha():
            new_string += char.lower()

    return True if new_string == new_string[::-1] else False


print(palindrome_check(initial_str))
