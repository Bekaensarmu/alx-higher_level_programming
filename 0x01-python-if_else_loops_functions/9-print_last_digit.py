def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
number = 12345
result = print_last_digit(number)
print("Last digit:", result)
