



# Every fourth hour, all employees have a break, so they don't work for an hour. '
# It is the only break for the employees, because they don't need rest, nor have a personal life.'
#         ' Calculate the time needed to answer all the student's
# questions and print it in the following format: "Time needed: {time}h."
# Input / Constraints
# •	On the first three lines -  each employee efficiency -  integer in the range [1 - 100]
# •	On the fourth line - students count – integer in the range [0 – 10000]
# •	Input will always be valid and in the range specified
# Output
# •	Print a single line: "Time needed: {time}h."
# for_one_hour = 0
# hour_works = 0
# for i in range(3):
#     employee = int(input())
#     for_one_hour += employee
# students = int(input())
#
# while students > 0:
#     students -= for_one_hour
#     hour_works += 1
#     if hour_works % 4 == 0:
#         hour_works += 1
#
# print(f"Time needed: {hour_works}h.")


#
# import sys
# from io import StringIO
#
# input1 = """3
# 2
# 5
# 40"""
#
# sys.stdin = StringIO(input1)

import math

first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())

employees_efficiency = math.ceil(students / (first_employee + second_employee + third_employee))
for i in range(1,employees_efficiency):
    if i % 3 == 0:
        employees_efficiency += 1
# break_for_hour = employees_efficiency//3 # 80/100
print(f"Time needed: {employees_efficiency}h.")































