#
# data = input()
# courses = {}
# while not data == "end":
#
#     course_name, student_name = data.split(' : ')
#
#     if course_name not in courses:
#         courses[course_name] = []
#     courses[course_name].append(student_name)
#
#
#     data = input()
#
# # sorted_courses =sorted(courses.items(),key=lambda kvpt: kvpt[0]) #, reverse=True
# for course_name,students in courses.items():
#     print(f"{course_name}: {len(students)}")
#     for name in students:
#         print(f"-- {name}")


def add_course(dict,course, name):
    if course not in dict:
        dict[course] = []
    dict[course].append(name)
    return dict


courses = {}
command = input()
while not command == 'end':
    course_name, student_name = command.split(" : ")
    add_course(courses,course_name, student_name)

    command = input()

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")



























