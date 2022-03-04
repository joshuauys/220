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

    for i in range(in_text_string.count("\n") + 1):
        print(in_text_string)
        in_text_lines = in_text_file.readline()
        number_of_hours = in_text_line[-2:]
        pay rate = in_text_line[-8:-2]

        print(number_of_hours)

        # in_text_string.find("\n")
        # in_text_lines = in_text_string

    pay = number_of_hours * pay_rate + number_of_hours * 1.65

    out_text_file = open(out_file_name, "w")
    out_text_file.write(pay)

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

    out_text_file = open(friend_name + ".txt", "w")
    out_text_file.write()

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

def encode_better(message: str, key: str):
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

    return(encoded_message)

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_text_file = open(file_name, "r")
    in_text_string = in_text_file.read()
    out_text_file = open(pad_file_name, "w")
    out_text_file.write(encode_better(in_text_string, ))

if __name__ == '__main__':
    pass
