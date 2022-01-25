"""
Name: Joshua Uys
MeansCalculator.py

Problem: This program aims to calculate means from user input

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def means():
    input_count = eval(input("How many values are you entering? "))

    input_value = 0
    rms_accum = 0
    harmonic_accum = 0
    geometric_accum = 1

    for i in range(input_count):
        input_value = eval(input("What value do you want to average? "))

        rms_input_squared = 0
        rms_input_squared = input_value ** 2
        rms_accum += rms_input_squared
        rms_average = rms_accum / input_count
        rms = rms_average ** 0.5

        recipricals = 1 / input_value
        harmonic_accum += recipricals
        harmonic_mean = input_count / harmonic_accum

        geometric_accum = geometric_accum * input_value
        geometric_mean = geometric_accum ** (1 / input_count)

    print("Root mean square:", round(rms, 3))
    print("Harmonic mean:", round(harmonic_mean, 3))
    print("Geometric mean:", round(geometric_mean, 3))


means()


