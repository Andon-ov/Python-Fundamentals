# import sys
# from io import StringIO
#
# input1 = """%InvalidName%<Croissant>|2|10.3$
# %Peter%<Gum>1.3$
# %Maria%<Cola>|1|2.4
# %Valid%<Valid>valid|10|valid20$
# %George%<Croissant>|2|10.3$
# %Peter%<Gum>|100|11.3$
# %Maria%<Cola>|1|2.4$
# end of shift"""
#
# sys.stdin = StringIO(input1)
#
# import re
# income = 0
# # regex = r"%([A-Z][a-z]+)%<([A-Z][a-z]+)>\w*\|(\d*)\|[a-z]*?(\d*[\.\d*]+)\$" # 50\100
#
# # regex = r"^%([A-Z][a-z]+)%[^|$%.]*<([A-Z][a-z]+)>[^|$%.]*\w*\|(\d+)\|?[^|$%.]*?([\d+][\.\d]+)\$" # 70/100
#
# regex = r"^%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.]*?([-+]?[0-9]*\.?[0-9]+([-+]?[0-9]+)?)\$" #100\100
# data = input()
# while not data == "end of shift":
#
#     match = re.findall(regex,data)
#     if match:
#
#         print(f"{match[0][0]}: {match[0][1]} - {(int(match[0][2])* float(match[0][3])):.2f}")
#         income += int(match[0][2])* float(match[0][3])
#
#     data = input()
# print(f"Total income: {income:.2f}")

# ToDo 50/100


import sys
from io import StringIO

input1 = """%InvalidName%<Croissant>|2|10.3$
%Peter%<Gum>1.3$
%Maria%<Cola>|1|2.4
%Valid%<Valid>valid|10|valid20$
%George%<Croissant>|2|10.3$
%Peter%<Gum>|100|11.3$
%Maria%<Cola>|1|2.4$
end of shift"""

sys.stdin = StringIO(input1)

import re
# regex = r"^%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.]*?([-+]?[0-9]*\.?[0-9]+([-+]?[0-9]+)?)\$" #100\100
# regex = r"^%([A-Z][a-z]+)%[^|$%.]*<([A-Z][a-z]+)>[^|$%.]*\w*\|(\d+)\|?[^|$%.]*?([\d+][\.\d]+)\$" # 70/100
regex = r"^%([A-Z][a-z]+)%<(\w+)>\|(\d+)\|?([-+]?[0-9]*\.?[0-9]+([-+]?[0-9]+)?)\$"

command = input()
price_sum = 0
while not command == "end of shift":
    matches = re.match(regex, command)
    if matches:

        print(f"{matches.groups()[0]}: {matches.groups()[1]} - {int(matches.groups()[2]) * float(matches.groups()[3]):.2f}")
        price_sum += int(matches.groups()[2]) * float(matches.groups()[3])

    command = input()
print(f"Total income: {price_sum:.2f}")