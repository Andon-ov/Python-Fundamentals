# import math
# number_of_students = int(input())
# course_lectures = int(input())
# additional_bonus = int(input())
# max_bonus = 0
# max_lectures = 0
# for _ in range(number_of_students):
#     student_attendances = int(input())
#     if student_attendances > max_lectures and student_attendances <= course_lectures:
#         max_lectures = student_attendances
#
#     total_bonus = student_attendances / course_lectures *(5 + additional_bonus)
#     if total_bonus > max_bonus:
#         max_bonus = total_bonus
#
# print(f'Max Bonus: {math.ceil(max_bonus)}.')
# print(f'The student has attended {max_lectures} lectures.')


from math import ceil
number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())

lectures = 0
max_bonus = 0
for i in range(number_of_students):
    attendances_for_each_student = int(input())

    total_bonus = attendances_for_each_student / total_number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        lectures = attendances_for_each_student

print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {lectures} lectures.')






