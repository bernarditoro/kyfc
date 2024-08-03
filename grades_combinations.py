from itertools import combinations_with_replacement, permutations

from tabulate import tabulate


grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2}

grades = (s.upper() for s in 'abcd')

reply = """\nSo I've expanded the script to work with more input (though hardcoded):

* You offer 7 courses
* You want to get the best combination of grades that will give you a minimum CGPA of 4.50 (in a system of 5.0 CGPA)
* You want to completely avoid Es and Fs
* CGPA = sum(units * grade points) / sum(units)\n"""

print(reply)

courses_tuple = ('COS121', 'GST121', 'MTH121', 'PHY121', 'PHY128', 'CSC121', 'CSC122')
courses_units = (3, 2, 2, 2, 1, 3, 2)

grades_combinations = list(combinations_with_replacement(grades, len(courses_units)))

all_grades_combinations = []

for combo in grades_combinations:
    all_grades_combinations += list(permutations(combo))
 
all_grades_combinations = list(set(all_grades_combinations))

preferred_grades_combination = []

for grades_combination in all_grades_combinations:
    credit_hours = sum([s * grade_points[y] for s, y in zip(courses_units, grades_combination)])
    credit_units = sum(courses_units)

    if credit_hours/credit_units > 4.5:
        preferred_grades_combination.append(grades_combination)

table = tabulate(preferred_grades_combination, headers=courses_tuple, tablefmt='grid')

with open('grades.txt', 'w') as f:
    f.write(table)

print('Table written to grades.txt!')

