from itertools import combinations_with_replacement, permutations, zip_longest

from tabulate import tabulate

import math

from typing import List


class KYFC: # Means 'Keep Your First Class'. Don't judge me...that's the reason for the script in the first place!
    def __init__(self) -> None:
        intro = """\nSo I've expanded the script (though hardcoded):

        * You already have a CGPA
        * You want to get the all combination of grades that will give you a minimum CGPA of 4.50 (in a system of 5.0 CGPA)
        * You want to completely avoid Es and Fs
        * CGPA = sum(units * grade points) / sum(units)
        * You know what to expect in some courses in the current semester (or maybe not)\n"""

        print(intro)

        self.degree_classes = {'f': (4.5, 5.0), 'su': (3.5, 4.49), 'sl': (2.4, 3.49), 't': (1.5, 2.39), 'p': (1.0, 1.49)}
        # f: First class, su: Second class Upper, sl: Second class Lower, t: Third class, p: Pass

        self.grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
        self.allowed_grades = (s.upper() for s in 'abcd')

        self.courses_list = [['COS111', 'GST111', 'MTH111', 'PHY111', 'PHY117', 'STA111', 'CSC111', 'CSC112'], ['COS121', 'GST121', 'MTH121', 'PHY121', 'PHY128', 'CSC121', 'CSC122']]
        self.credit_hours = [[3, 2, 2, 2, 1, 3, 3, 2], [3, 2, 2, 2, 1, 3, 2]]
        self.grades = [['A', 'B', 'A', 'A', 'A', 'A', 'A', 'B'], ['A', '', '', 'B', 'B', '', '']]

        self.set_grade_combinations()

    def set_grade_combinations(self) -> None:
        combinations = list(combinations_with_replacement(self.allowed_grades, len(self.credit_hours[-1])))

        self.all_grades_combinations = []

        for c in combinations:
            self.all_grades_combinations += list(permutations(c))
        
        self.all_grades_combinations = list(set(self.all_grades_combinations))

    def calculate_gpa(self, credit_hours: List[int], grades: List[str]) -> float:
        quality_points = sum([s * self.grade_points[y] for s, y in zip_longest(credit_hours, grades)])
        sum_credit_hours = sum(credit_hours)

        gpa = quality_points / sum_credit_hours

        # Since GPAs are always truncated after 2 decimals...
        gpa = float(f"{math.trunc(gpa)}.{str(gpa).split('.')[1][:2]}")

        return gpa

    def calculate_cgpa(self, cumulative_credit_hours: List[List[int]], cumulative_grades: List[List[str]]) -> float:
        total_quality_points = 0
        total_credit_hours = 0

        for hours, grades in zip(cumulative_credit_hours, cumulative_grades):
            total_quality_points += sum([h * self.grade_points[g] for h, g in zip(hours, grades)])
            total_credit_hours += sum(hours)

        cgpa = total_quality_points / total_credit_hours

        # Since GPAs are always truncated after 2 decimals...
        cgpa = float(f"{math.trunc(cgpa)}.{str(cgpa).split('.')[1][:2]}")

        return cgpa

    def export_cgpa(self) -> None:
        for credit_hours, grades, courses in zip(self.credit_hours[:-1], self.grades[:-1], self.courses_list[:-1]): # We don't want the last item as it would be the current semester
            gpa = self.calculate_gpa(credit_hours, grades)

            table_header = [courses.copy() + ['GPA']]

            table_body = [grades.copy() + [gpa]]

            table = tabulate(table_body, headers=table_header, tablefmt='pipe')
            
            with open('cgpa.txt', 'a') as f:
                f.write(table)
                f.write('\n\n')

        with open('cgpa.txt', 'a') as f:
            cgpa = self.calculate_cgpa(self.credit_hours[:-1], self.grades[:-1])

            f.write(f'Your CGPA is {cgpa}\n\n')

        print('Past semesters\' GPA have been exported to cgpa.txt!')
    
    def export_kyfc_combinations(self, use_cgpa=True, degree_class='f') -> None:
        kyfc_grades_combinations = [] # I know I've included combinations for other classes, but no, I'm not changing it

        for grades_combination in self.all_grades_combinations:
            if all(p == '' or g == p for g, p in zip_longest(grades_combination, self.grades[-1])):
                grades = self.grades[:-1]
                grades.append(grades_combination)

                cgpa = self.calculate_cgpa(self.credit_hours, grades)

                gpa = self.calculate_gpa(self.credit_hours[-1], grades_combination)

                grade_value = cgpa if use_cgpa else gpa

                if self.degree_classes[degree_class][0] <= grade_value <= self.degree_classes[degree_class][1]:
                    grades_combination_list = list(grades_combination) + [gpa, cgpa]

                    kyfc_grades_combinations.append(grades_combination_list)

        table_header =  self.courses_list[-1].copy() + ['GPA', 'CGPA']

        table = tabulate(kyfc_grades_combinations, headers=table_header, tablefmt='pipe')

        with open('kyfc_grades.txt', 'w') as f:
            f.writelines(['Here are some grades combinations you should anticipate if you plan on keeping your first class:\n\n', table])

        print('KYFC grades have been exported to kyfc_grades.txt!')


if __name__ == '__main__':
    kyfc = KYFC()

    kyfc.export_kyfc_combinations(use_cgpa=False)

    # kyfc.export_cgpa()
