from itertools import combinations_with_replacement

from tabulate import tabulate


grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2}

grades = (s.upper() for s in 'abcd')

reply = """\nSo this initial script is built with stern constraints for testing purposes which are:

* You offer 4 courses:
    CSC111 (3 units)
    STA111 (3 units)
    GST111 (2 units)
    PHY117 (1 unit)
* You want to get the best combination of grades that will give you a minimum CGPA of 4.50 (in a system of 5.0 CGPA)
* You want to completely avoid Es and Fs
* CGPA = sum(units * grade points) / sum(units)\n"""

print(reply)

courses_tuple = ('CSC111', 'STA111', 'GST111', 'PHY117')
courses_units = (3, 3, 2, 1)

grades_combinations = list(combinations_with_replacement(grades, 4))

preferred_grades_combination = [] # This contains the grade combinations in tuples

for grades_combination in grades_combinations:
    credit_hours = sum([s * grade_points[y] for s, y in zip(courses_units, grades_combination)])
    credit_units = sum(courses_units)

    if credit_hours/credit_units > 4.5:
        preferred_grades_combination.append(grades_combination)

print (tabulate(preferred_grades_combination, headers=courses_tuple, tablefmt='grid'))

