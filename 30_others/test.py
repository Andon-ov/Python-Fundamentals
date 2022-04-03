# import sys
# from io import StringIO
#
# input1 = """3 2
# 1 5 3 7
# 3 1
# 5 7 1 3"""
# input2 = """"""
# input3 = """"""
#
# sys.stdin = StringIO(input1)
# happiness = 0
# n, m = [int(x) for x in input().split()]
# my_list = [int(x) for x in input().strip().split()]
# a_list = {int(x) for x in input().strip().split()}
# b_list = {int(x) for x in input().strip().split()}
# for i in my_list:
#     if i in a_list:
#         happiness += 1
#     if i in b_list:
#         happiness -= 1
# print(happiness)

# import sys
# from io import StringIO
#
# input1 = """ 16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66"""
# input2 = """"""
# input3 = """"""
#
# sys.stdin = StringIO(input1)
# a = int(input())
# a_list = {int(x) for x in input().strip().split()}
# n = int(input())
# for _ in range(n):
#     command = input().split()
#     numbers = {int(x) for x in input().strip().split()}
#     if command[0] == "intersection_update":
#         a_list.intersection_update(numbers)
#     elif command[0] == "update":
#         a_list.update(numbers)
#     elif command[0] == "symmetric_difference_update":
#         a_list.symmetric_difference_update(numbers)
#     elif command[0] == "difference_update":
#         a_list.difference_update(numbers)
# print(sum(a_list))


# import sys
# from io import StringIO
#
# input1 = """qA2"""
# input2 = """"""
# input3 = """"""
#
# sys.stdin = StringIO(input1)
#
#
# def all_num(string):
#     for i in s:
#         if i.isalnum():
#             return True
#     return False
#
#
# def alpha(string):
#     for i in s:
#         if i.isalpha():
#             return True
#     return False
#
#
# def digit(string):
#     for i in s:
#         if i.isdigit():
#             return True
#     return False
#
#
# def lower(string):
#     for i in s:
#         if i.islower():
#             return True
#     return False
#
#
# def upper(string):
#     for i in s:
#         if i.isupper():
#             return True
#     return False
#
#
# s = input()
# if all_num(s):
#     print('True')
# else:
#     print("False")
# if alpha(s):
#     print('True')
# else:
#     print("False")
# if digit(s):
#     print('True')
# else:
#     print("False")
# if lower(s):
#     print('True')
# else:
#     print("False")
# if upper(s):
#     print('True')
# else:
#     print("False")

# import sys
# from io import StringIO
#
# input1 = """2
# 1 2"""
# input2 = """"""
# input3 = """"""

# sys.stdin = StringIO(input1)
# n = input()
# my_list = [int(x) for x in input().strip().split()]
# my_list = tuple(my_list)
# print(hash(my_list))

# import sys
# from io import StringIO
#
# input1 = """100,000,000.000"""
# input2 = """"""
# input3 = """"""
#
# sys.stdin = StringIO(input1)
#
# import re
# text = input()
#
# match = re.split(r"\.|,",text)
# for i in match:
#     print(i)

import sys
from io import StringIO

# input1 = """7
# UK
# China
# USA
# France
# New Zealand
# UK
# France"""
# input2 = """"""
# input3 = """"""
#
# sys.stdin = StringIO(input1)
# # n = int(input())
# # country = []
# # for _ in range(n):
# #     data = input()
# #     country.append(data)
# # print(len(set(country)))
#
# import sys
# from io import StringIO
#
# input1 = """6"""
#
#
# sys.stdin = StringIO(input1)


# def fizzBuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#
#             if i % 3 == 0:
#                 if not i % 5 == 0:
#                     print("Fuzz")
#
#             if i % 5 == 0:
#                 if not i % 3 == 0:
#                     print("Buzz")
#
#         else:
#             print(i)
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     fizzBuzz(n)

#
# def staircase(n):
#     for i in range(1,n+1):
#         space = " "
#         print(f"{space * abs(i - n)}{'#' * i }")
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     staircase(n)

