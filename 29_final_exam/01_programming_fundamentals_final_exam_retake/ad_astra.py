# import sys
# from io import StringIO
#
# input1 = """#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|"""
#
# sys.stdin = StringIO(input1)

# import re
#
# text = input()
# food_for_days = 2000
# sums = 0
# regex = r"([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
# valid_data = re.findall(regex, text)
# for i in valid_data:
#
#     calories = int(i[3])
#     sums += calories
#
# print(f"You have food to last you for: {sums//food_for_days} days!")
#
# for i in valid_data:
#     print(f"Item: {i[1]}, Best before: {i[2]}, Nutrition: {i[3]}")


import sys
from io import StringIO

input1 = """#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|"""
input2 = """Hello|#Invalid food#19/03/20#450|$5*(@"""
input3 = """$$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|"""

sys.stdin = StringIO(input2)

import re

regex = r"(#|\|)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
calories = 0
text = input()
match = re.findall(regex, text)
for i in match:

    calories += int(i[3])

print(f"You have food to last you for: {calories//2000} days!")
for j in match:
    print(f"Item: {j[1]}, Best before: {j[2]}, Nutrition: {j[3]}")