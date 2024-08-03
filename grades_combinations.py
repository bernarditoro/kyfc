from itertools import combinations_with_replacement, permutations

from tabulate import tabulate

import math


grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}

grades = (s.upper() for s in 'abcd')

reply = """\nSo I've expanded the script to work with more input (though hardcoded):

* You offer 7 courses
* You want to get the best combination of grades that will give you a minimum CGPA of 4.50 (in a system of 5.0 CGPA)
* You want to completely avoid Es and Fs
* CGPA = sum(units * grade points) / sum(units)\n"""

print(reply)

courses_list = ['COS121', 'GST121', 'MTH121', 'PHY121', 'PHY128', 'CSC121', 'CSC122', 'GPA']
credit_hours = (3, 2, 2, 2, 1, 3, 2)

grades_combinations = list(combinations_with_replacement(grades, len(credit_hours)))

all_grades_combinations = []

for combo in grades_combinations:
    all_grades_combinations += list(permutations(combo))
 
all_grades_combinations = list(set(all_grades_combinations))

preferred_grades_combination = []

for grades_combination in all_grades_combinations:
    quality_points = sum([s * grade_points[y] for s, y in zip(credit_hours, grades_combination)])
    sum_credit_hours = sum(credit_hours)

    gpa = quality_points / sum_credit_hours

    # Since GPAs are always truncated after 2 decimals...
    gpa = float(f"{math.trunc(gpa)}.{str(gpa).split('.')[1][:2]}")

    if gpa > 4.5:
        grades_combination_list = list(grades_combination)
        grades_combination_list.append(gpa)

        preferred_grades_combination.append(grades_combination_list)

table = tabulate(preferred_grades_combination, headers=courses_list, tablefmt='grid')

with open('grades.txt', 'w') as f:
    f.write(table)

print('Table written to grades.txt!')

