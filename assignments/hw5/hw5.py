"""
Name: Joshua Uys
hw5.py

Strings and Lists

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def name_reverse():
    input = input("Enter a name (First Last)")
    reversed_name_list = input.split(" ")
    last_name = reversed_name_list[1]
    first_name = reversed_name_list[0]
    print(last_name, ",", first_name)

def company_name():
    domain = input("Enter a domain:")

    cut_front = domain.replace("www.", "")
    cut_end = cut_front.replace(".com", "")
    print(cut_end)

def initials():
    number_of_students = eval(input("How many students are in the class?"))
    for i in range(number_of_students):
        print("What is the name of student", i + 1)
        student_name = input()
        first_initial = student_name[0]
        second_initial_position = student_name.find(" ")
        second_initial = student_name[second_initial_position + 1]
        print(first_initial, second_initial)

def names():
    names = input("Enter a list of names (First Last) seperated by a comma")
    names_list = names.split(", ")
    number_of_names = names.count(", ")
    for i in range(number_of_names + 1):
        print = ""
        first_name_initial = names_list[i]

    print(names_list[i], end = " ")

# names()
# not complete

def thirds():
    sentences = ""
    number_of_sentences = eval(input("Enter the number of sentences: "))
    for i in range(number_of_sentences):
        print("Enter sentence", i + 1, end = "")
        sentences += input("") + "\n"
    sentence_list = sentences.split("\n")
    print(list)
    for i in range(number_of_sentences):
        print(str(sentence_list[i])[0:len(sentence_list[i]):3])

def word_average():
    sentence = input("Enter a sentence: ")
    sentence_list = sentence.split(" ")
    average_length_accum = 0
    sum_length_accum = 0

    list_length = len(sentence_list)
    for i in range(list_length):
        sum_length_accum += len(sentence_list[i])
    average_length_accum  = sum_length_accum / len(sentence_list)
    print(average_length_accum)

# word_average()

def pig_latin():
    normal_sentence = input("Enter a sentence to convert to pig latin")
    normal_sentence_list = normal_sentence.split(" ")
    pig_latin_accum = ""

    for i in range(len(normal_sentence_list)):

        first_letter = str(normal_sentence_list[i])[0]
        remove_first_letter = str(normal_sentence_list[i]).replace(first_letter, "")
        new_word = remove_first_letter + first_letter + "ay" + " "
        pig_latin_accum += new_word

    print(pig_latin_accum.lower())

pig_latin()

