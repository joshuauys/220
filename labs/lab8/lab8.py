"""
Name: Joshua Uys
lab8.py

Grades

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    in_text_file = open(in_file_name, "r")
    lines_list = in_text_file.readlines()

    number_of_lines = len(lines_list)

    class_average_accum = 0
    eligible_student_accum = 0
    output_line = ""

    # seperating the student's name from the grades and weights
    for i in range(number_of_lines):
        current_line = lines_list[i]
        location_of_colon = current_line.find(":")
        name = current_line[0 : location_of_colon] + "'s"
        to_remove = current_line[0 : location_of_colon + 2]
        grades = current_line.replace(to_remove, "")

        results_list = grades.split()

        even_weighting = 0
        odd_grade = 1

        grades_list = []
        weight_list = []

        # seperating the long string of numbers into a weights list and grades list
        for i in range(len(results_list ) // 2):

            grades_list += results_list[odd_grade:odd_grade + 1]
            weight_list += results_list[even_weighting:even_weighting + 1]

            even_weighting += 2
            odd_grade += 2

        weights_sum = 0
        for i in range(len(weight_list)):
            weights_sum += eval(weight_list[i])

        weight_adds_to_100 = True

        if weights_sum < 100:
            weight_adds_to_100 = False
            output_line += name
            output_line += "average: "
            output_line += "Error: The weights are less than 100."

        if weights_sum > 100:
            weight_adds_to_100 = False
            output_line += name
            output_line += "average: "
            output_line += "Error: The weights are more than 100."

        average_grade_accum = 0

        if weights_sum == 100:
            for i in range(len(weight_list)):
                average_grade_accum += int(weight_list[i]) * int(grades_list[i]) / 100
            output_line += name
            output_line += "average: "
            output_line += str(average_grade_accum)
            eligible_student_accum += 1
            class_average_accum += average_grade_accum

        output_line += "\n"
    output_line += "Class average: "
    output_line += str(class_average_accum / eligible_student_accum)

    out_text_file = open(out_file_name, "w")
    out_text_file.write(output_line)

    in_text_file.close()
    out_text_file.close()

# weighted_average("Grades.txt", "Output.txt")