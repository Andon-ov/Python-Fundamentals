# import sys
# from io import StringIO
#
# input1 = """8
# @###Val1d1teM@###
# @#ValidIteM@#
# ##InvaliDiteM##
# @InvalidIteM@
# @#FreshFisH@#
# @###Brea0D@###
# @##Che0!0sE@##
# @##Che46sE@###
# """
#
# sys.stdin = StringIO(input1)
#
# import re
# n = int(input())
# regex = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"  #100/100
# # regex = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\1)" #80/100
# # regex = r"(@#+)([A-Z][a-z*\d*A-Z*]{5,})(\1)"  # 70/100
#
#
# for i in range(n):
#     barcode = input()
#     match = re.match(regex, barcode)
#     if match:
#         barcode_group = ''
#
#         for r in match.group(1):
#             if r.isdigit():
#                 barcode_group += r
#         if barcode_group == '':
#             print("Product group: 00")
#
#         else:
#             print(f"Product group: {barcode_group}")
#
#     else:
#         print("Invalid barcode")


# import sys
# from io import StringIO
#
# input1 = """6
# @###Val1d1teM@###
# @#ValidIteM@#
# ##InvaliDiteM##
# @InvalidIteM@
# @#Invalid_IteM@#
# @#ValiditeM@#"""
# input2 = """3
# @#FreshFisH@#
# @###Brea0D@###
# @##Che4s6E@##"""
#
#
# # sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
#
# import re
# regex = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
# barcode = []
# n = int(input())
# for i in range(n):
#     string = input()
#     match = re.findall(regex,string)
#
#     if match:
#         barcode.append(*match)
#     else:
#         barcode.append("Invalid barcode")
#
# for word in barcode:
#     if word == "Invalid barcode":
#         print("Invalid barcode")
#     else:
#         number = ''
#         for d in word:
#             if d.isdigit():
#                 number += d
#         if number == "":
#             number = "00"
#         print(f"Product group: {number}")
#         number = ''


import sys
from io import StringIO

input1 = """6
@###Val1d1teM@###
@#ValidIteM@#
##InvaliDiteM##
@InvalidIteM@
@#Invalid_IteM@#
@#ValiditeM@#"""
input2 = """3
@#FreshFisH@#
@###Brea0D@###
@##Che4s6E@##"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

import re

regex = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

n = int(input())
for i in range(n):
    string = input()
    match = re.match(regex, string)

    if match:
        group = ""
        for d in match.group():
            if d.isdigit():
                group += d

        if group == "":
            print(f"Product : 00")
        else:
            print(f"Product : {group}")
    else:
        print("Invalid barcode")
