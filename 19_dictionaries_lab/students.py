# data = input()
# courses = {}
# while ":" in data:
#     students_name, id, course_name = data.split(":")
#     if course_name not in courses:
#         courses[course_name] = {}
#     courses[course_name][id] = students_name
#
#     data = input()
# searched_courses = data
# searched_courses_name_as_list = searched_courses.split("_")
# searched_courses = ' '.join(searched_courses_name_as_list)
#
# # ако проверяваме дали го има курса
# # for course_name in courses:
# #     if course_name == searched_courses:
# for id, name in courses[searched_courses].items():
#     print(f'{name} - {id}')

courses = {}
command = input()
while ':' in command:
    students_name, id, course_name = command.split(":")
    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][id] = students_name

    command = input()
searched_courses = command

searched_courses_name_as_list = searched_courses.split("_")
searched_courses = ' '.join(searched_courses_name_as_list)

# for course_name in courses:
#     if course_name == searched_courses:

for id, name in courses[searched_courses].items():
    print(f'{name} - {id}')
