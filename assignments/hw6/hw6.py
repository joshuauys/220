"""
Name: Joshua Uys
hw6.py

String formatting

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def cash_converter():
    integer = eval(input("Enter an integer"))
    string = "This is ${:.2f}".format(integer)
    print(string)

def encode():
    message = input("Enter a message: ")
    key = eval(input("Enter a key: "))
    message_length = len(message)
    encoded_message = ""

    for i in range(message_length):
        encoded_message += chr(ord(message[i]) + key)

    print(encoded_message)

def sphere_area(radius: float):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

def sphere_volume(radius: float):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume

def sum_n(number: int):
    total = 0
    for i in range(number + 1):
        total += (i)
    return total

def sum_n_cubes(number: int):
    total = 0
    for i in range(number + 1):
        total += i ** 3
    return total

def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")

    message_length = len(message)
    key_length = len(key)

    key_list = []

    encoded_message = ""

    for i in range(key_length):
        key_list.append(ord(key[i]) - 65)
    print("key list: ",key_list)

    for i in key_list:
        key_unicode = i
        for x in range(message_length):
            encoded_message += chr(ord(message[x]) - 65 + key_unicode)
            print(chr(ord(message[x]) - 65 + key_unicode))
            # print(chr(ord(message[x]) - 65 + key_unicode))
            # print(ord(message[x]) - 65 + key_unicode)

    print(encoded_message)
