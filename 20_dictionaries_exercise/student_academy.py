# grades = {}
# n = int(input())
# for i in range(n):
#     student_name = input()
#     grade = float(input())
#
#     if student_name not in grades:
#         grades[student_name] = []
#     grades[student_name].append(grade)
#
# filtered_grade  ={}
#
# for key, value in grades.items():
#     avr_grade = sum(value)/len(value)
#     if avr_grade >= 4.50:
#         filtered_grade[key] = avr_grade
# for key,value in filtered_grade.items():
#     print(f"{key} -> {(value):.2f}")

def students_grades(dict,name,grade):
    if name not in dict:
        dict[name] = []
    dict[name].append(grade)
    return dict


student_academy = {}
n = int(input())
for _ in range(n):
    name = input()
    grade = float(input())

    students_grades(student_academy,name,grade)

for key,value in student_academy.items():
    if sum(value)/len(value) >= 4.50:
        print(f"{key} -> {(sum(value)/len(value)):.2f}")



















