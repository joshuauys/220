"""
Name: <your name goes here – first and last>
hw7.py

Problem: File processing

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def number_words(in_file_name: str, out_file_name: str):
    in_text_file = open(in_file_name, "r")
    in_text_string = in_text_file.read()
    in_text_list = in_text_string.split()

    out_text_file = open(out_file_name, "w")

    for i in range(len(in_text_list)):
        numbering = str(i + 1)
        out_text_file.write(numbering + " " + in_text_list[i] + "\n")

    in_text_file.close()
    out_text_file.close()

def hourly_wages(in_file_name: str, out_file_name: str):
    in_text_file = open(in_file_name, "r")
    in_text_string = in_text_file.read()
    in_text_list = in_text_file.readlines()

    for line in in_text_file:
        print("x")

    for i in range(in_text_string.count("\n") + 1):
        print(in_text_string)
        in_text_lines = in_text_file.readline()
        number_of_hours = in_text_lines

        print(number_of_hours)

        # in_text_string.find("\n")
        # in_text_lines = in_text_string

    # number_of_hours = in_text_line[-2:]

    out_text_file = open(out_file_name, "w")

hourly_wages("hourly_wages.txt", "outfile.txt")
# not complete

def calc_check_sum(isbn: str):
    ISBN = isbn.replace("-", "")
    length = len(ISBN)
    product = 10
    ISBN_accum = 0
    for i in range(length):
        ISBN_accum += (eval(ISBN[i]) * product)
        product -= 1

def send_message(file_name, friend_name):
    in_text_file = open(file_name, "r")
    in_text_string = in_text_file.read()

    print(in_text_string)

    out_text_file = open(friend_name + ".txt", "w")
    out_text_file.write("Message2")

# send_message("hourly_wages.txt", "name")

# incomplete

def encode(message: str, key: int):
    # message = input("Enter a message: ")
    # key = eval(key)
    message_length = len(message)
    encoded_message = ""

    for i in range(message_length):
        encoded_message += chr(ord(message[i]) + key)

    print(encoded_message)
    return encoded_message

def send_safe_message(file_name: str, friend_name: str, key: int):
    in_text_file = open(file_name, "r")
    in_text_list = in_text_file.readlines()
    length = len(in_text_list)

    encoded_message = ""

    for i in range(length):
        encoded_message += (encode(in_text_list[i], key)) + "\n"

    out_text_file = open(friend_name + ".txt", "w")
    out_text_file.write(encoded_message)

# send_safe_message("hourly_wages.txt", "name", 5)

# go back to txt files, create new "{name}.txt"

def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")

    message_length = len(message)
    key_length = len(key)
    key_tracker = 0
    key_list = []

    encoded_message = ""
    for x in range(message_length // key_length + message_length % key_length):
        for i in range(key_length):
            key_list.append(ord(key[i]) - 65)

    for i in range(message_length):
        unicode_message = ord(message[i]) - 65
        unicode_key = key_list[key_tracker]
        unicode_shifted_message = (unicode_message + unicode_key) % 58
        shifted_message = chr(unicode_shifted_message + 65)

        key_tracker += 1

        encoded_message += shifted_message

    print(encoded_message)

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
