#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))

# Example usage:
input_list = [1, 2, 3, 4, 5]
multiplier = 2

result_list = multiply_list_map(input_list, multiplier)
print(result_list)


