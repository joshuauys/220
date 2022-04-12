"""
Name: Joshua Uys

algorithms.py

Loops and Lists

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def read_data(filename):
    file_string = open(filename, "r").read().replace("\n", " ")
    file_list = file_string.split(" ")

    return file_list

# read_data("data_sorted.txt")

# list = [75, 82, 90, 97, 100]

def is_in_linear(search_val, values):
    search_position = 0
    list_length = len(values)

    while search_val != values[search_position] and search_position != list_length - 1:
        search_position += 1

    if values[search_position] == search_val:
        return True
    else: return False


# print(is_in_linear(97, list))
