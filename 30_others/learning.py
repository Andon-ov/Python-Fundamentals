# # проверка дали е число или текс
# txt = "50800"
# x = txt.isdigit()
# print(x) #True
#
# # обръщане на стринг във инт
# nums_as_string = ['1','2','3']
# # лист копреханшан
# nums = [int(num) for num in nums_as_string]
# # ланда със мап
# nums_2 = list(map(lambda x: int(x),nums_as_string))
# # референция към функция с мап
# nums_3 = list(map(int,nums_as_string))
#
# nums_as_string = ['1','2','3']
# # филтър и мап със ламбда финкция (по стария и по бър метод) - преобразува елемент от стринг в инт - само четните
# res = list(filter(lambda el: el % 2 == 0, map(lambda el: int(el),nums_as_string)))
# # лист компрехеншан - преобразува елемент от стринг в инт - само четните
# res1 = [int(el) for el in nums_as_string if int(el) % 2 == 0]
#
# # Python String Method
# # The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# txt = "Company12"
# x = txt.isalnum()
# print(x)
#
# # The isalpha() method returns True if all the characters are alphabet letters (a-z).
# txt = "CompanyX"
# x = txt.isalpha()
# print(x)
#
# # The isdigit() method returns True if all the characters are digits, otherwise False.
# txt = "50800"
# x = txt.isdigit()
# print(x)
#
# # https://www.w3schools.com/python/python_ref_string.asp
#
# mylist = [True, True, True]
# x = all(mylist)
#
# word = "MyPass123"
#
# # def must_consist_only_of_letters_and_digits(word):
# letters_and_digits = word.isalnum()
# if letters_and_digits:
#     print("yes")
# print(letters_and_digits)
#
# важно
# from collections import defaultdict
#
# txt = "Hezzo"
#
# x = txt.replace("z", "l")
#
# print(x)
# word = "Hezzo"
#
# old_letter = "z"
# new_letter = "l"
# x = word.replace(old_letter, new_letter)
# print(x)
#
#
# a_dict = {"a": 1, "B": 2, "C": 3}
#
# new_key = "A"
# old_key = "a"
#
# a_dict[new_key] = a_dict.pop(old_key)
# print(a_dict)
#
#
# dict = {'Fur Elise': ['Beethoven', 'A Minor'], 'Moonlight Sonata': ['Beethoven', 'C# Major'], 'Sonata No.2': ['Chopin', 'B Minor'], 'Hungarian Rhapsody No.2': ['Liszt', 'C# Minor']}
#
# print(sorted(dict.items(), key =lambda kv:(kv[0], kv[1])))
# Сортираме листа аз първо по key после по value!!!
# text = 'Cyprus:Deuchland'
# if "Deuchland" in text:
#     print('yes')
#


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# print(dict(zip(keys,values)))

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)

# sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
# print(sampleDict["class"]["student"]["marks"]["history"])

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# final_dict = {employees[0]: defaults, employees[1]: defaults}
# print(final_dict)

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# # Keys to extract
# keys = ["name", "salary"]
#
# final_dict = {keys[0]: sample_dict["name"],keys[1]:sample_dict["salary"]}
# print(final_dict)


# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# # Keys to remove
# keys = ["name", "salary"]
#
# del sample_dict[keys[0]]
# del sample_dict[keys[1]]
# print(sample_dict)


# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print("yes")

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# # sample_dict['location'] = sample_dict.pop("city")
#
# sample_dict['location'] = sample_dict["city"]
# del sample_dict["city"]
#
# print(sample_dict)

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
#
# print(min(sample_dict.keys()))

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.get("model"))


# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# car["color"] = "red"
# print(car)

# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         leap = True
#         if year % 100 == 0:
#             leap = False
#             if year % 400 == 0:
#                 leap = True
#
#
#     return leap
#
# year = int(input())
# print(is_leap(year))


#
# n = int(input())
# integer_list = [2,3,6,6,5]
#
# max_number = max(integer_list)
# my_number = 0
# for i in integer_list:
#
#     if my_number < i < max_number :
#         my_number = i
# print(my_number)

# my_list = []
# python_students = {}
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     python_students[name] = score
#
# min_number = min(python_students.values()) # max_number[1]
# my_number = sys.maxsize
#
# for key,value in python_students.items():
#     if min_number < value < my_number:
#         my_number = value
#
# for key,value in python_students.items():
#     if value == my_number:
#         my_list.append(key)
#
# print("\n".join(sorted(my_list)))
# import sys
# from io import StringIO
#
# input1 = """2
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>"""
#
# sys.stdin = StringIO(input1)
#
#
# import re
# regex = r"([A-Za-z]+[\d\._\-]*)@[A-Za-z]+\.[A-Za-z]{1,3}"
# n = int(input())
# for i in range(n):
#     number = input()
#     matches = re.findall(regex,number)
#     if matches:
#         print(number)
#


# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# number = sum(student_marks[query_name])/len(student_marks[query_name])
# print(f"{number:.2f}")

# string = input()
# sub_string = input()
# count = 0
#
#
# print(count)

# import sys
# from io import StringIO
# import textwrap
#
# input1 = """6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft"""
#
# sys.stdin = StringIO(input1)

# text = input()
# n = int(input())
# print(textwrap.fill(text,n))

# from collections import deque
#
# d = deque()
# n = int(input())
# for i in range(n):
#     command = input()
#     command_split = command.split()
#     action = command_split[0]
#
#     if action == "append":
#         number = int(command_split[1])
#         d.append(number)
#     elif action == "appendleft":
#         number = int(command_split[1])
#         d.appendleft(number)
#     elif action == "pop":
#         d.pop()
#     elif action == "popleft":
#         d.popleft()
# print(*d)
import sys
from io import StringIO


input1 = """2
8 -10
3
5 6 7"""

sys.stdin = StringIO(input1)
s3 = []
s1 = set()
n = int(input())
s = [int(x) for x in input().split()]
for i in s:
    s1.add(i)

s2 = set()
b = int(input())
ss = [int(x) for x in input().split()]
for j in ss:
    s2.add(j)

s3 =[x for x in s1.symmetric_difference(s2)]
s3 = sorted(s3)
for i in s3:
    print(i)