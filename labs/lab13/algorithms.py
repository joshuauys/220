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

def is_in_linear(search_val, values):
    search_position = 0
    list_length = len(values)

    while search_val != values[search_position] and search_position != list_length - 1:
        search_position += 1

    if values[search_position] == search_val:
        return True
    else: return False

# def is_in_binary(search_val, values):
#     len_list = len(values)
#
#     bottom_index = 0
#     upper_index = len_list
#
#     found_position = False
#
#     while found_position == False:
#         middle_index = (upper_index - bottom_index) // 2
#
#         if search_val == values[middle_index]:
#             return middle_index
#             found_position = True
#         elif search_val < values[middle_index]:
#             upper_index = middle_index
#         elif search_val > values[middle_index]:
#             bottom_index = middle_index

def selection_sort(values):
    list_len = len(values)
    min_position = 0
    current_value = 0

    for i in range(list_len - 1):
        min_position = i

        for x in range(min_position + 1, list_len):
            if values[x] < values[min_position]:
                min_position = x

        if min_position != i:
            current_value = values[i]
            # swap two values
            values[i] = values[min_position]
            values[min_position] = current_value

    return values

def calc_area(rect):
    points_list = rect.getPoints()

    top_left = points_list[0]
    bottom_left = points_list[1]
    bottom_right = points_list[2]
    top_right = points_list[3]

    width = top_right.getX() - top_left.getX()
    height = bottom_right.getY() - top_right.getY()

    area = width * height
    return area

def rect_sort(rectangles):
    list_of_areas = []
    for i in range(len(rectangles)):
        list_of_areas.append(calc_area(rectangles[i]))
    return selection_sort(list_of_areas)




