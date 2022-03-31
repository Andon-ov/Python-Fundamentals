import sys
from io import StringIO

input1 = """>Invalid<<!5
>Invalid<<!5
>Invalid<<!5
Purchase"""

sys.stdin = StringIO(input1)

import re

# pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$"
# bought_furniture = []
# total_sum = 0
# command = input()
# while not command == "Purchase":
#     match = re.search(pattern, command)
#
#     if match:
#         furniture, price, quantity = match.groups()
#         bought_furniture.append(furniture)
#         total_sum += float(price) * int(quantity)
#
#     command = input()
#
# print(f'Bought furniture:')
# print('\n'.join(bought_furniture))
# print(f'Total money spend: {total_sum:.2f}')
# # ToDo 75/100 search

# import re
#
# pattern = r'>>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$'
# bought_furniture = []
# total_sum = 0
# command = input()
# while not command == "Purchase":
#     match = re.search(pattern, command)
#
#     if match:
#         furniture ,price, quantity = match.groups()
#         bought_furniture.append(furniture)
#         total_sum += float(price) * int(quantity)
#
#     command = input()
# print(f'Bought furniture:')
# print('\n'.join(bought_furniture))
# print(f'Total money spend: {total_sum:.2f}')
#  ToDo 75/100 search


# import re
#
# pattern = r'^>>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$'
# bought_furniture = []
# total_sum = 0
# command = input()
# while not command == "Purchase":
#     match = re.match(pattern, command)
#     if match:
#         obj = match.groupdict()
#         bought_furniture.append(obj["furniture_name"])
#         total_sum += float(obj["price"]) * int(obj['quantity'])
#
#     command = input()
# print(f'Bought furniture:')
# for mach in bought_furniture:
#     print(mach)
# print(f'Total money spend: {total_sum:.2f}')
# ToDo 100/100 match


# import re

# pattern = r'^>>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$'
# bought_furniture = []
# total_sum = 0
# command = input()
# while not command == "Purchase":
#
#     match = re.match(pattern, command,flags=re.MULTILINE)
#     if match:
#         furniture = match.group("furniture_name")
#         price = float(match.group("price"))
#         quantity = int(match.group('quantity'))
#
#         bought_furniture.append(furniture)
#         total_sum += float(price) * int(quantity)
#
#     command = input()
# print(f'Bought furniture:')
# for furniture in bought_furniture:
#     print(furniture)
# print(f'Total money spend: {total_sum:.2f}')
# ToDo 100/100 match


import re

regex = r"^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$"
sums = 0
furniture = []
text = input()
while not text == "Purchase":

    matches = re.findall(regex, text)
    if matches:
        furniture.append(matches[0][0])
        sums += float(matches[0][1]) * int(matches[0][2])

    text = input()

print("Bought furniture:")

for i in furniture:
    print(i)

print(f"Total money spend: {sums:.2f}")
# ToDo 100/100 findall
