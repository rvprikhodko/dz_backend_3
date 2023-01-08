initial_number = int(input())


def decimal_to_binary(number: int) -> str:
    converted_to_bin = ''

    while number:
        converted_to_bin += str(number % 2)
        number //= 2

    return converted_to_bin[::-1] if converted_to_bin else '0'


print(decimal_to_binary(initial_number))
