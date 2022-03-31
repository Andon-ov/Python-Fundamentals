# import re
# pattern = r"\d+"
# # https://pythex.org/
#
# text = input()
#
# while True:
#     if text:
#         valid_text = re.findall(pattern, text)
#         if valid_text:
#             print(*valid_text,end=' ')
#         text = input()
#     else:
#         break


import re

regex = r"\d+"
command = input()
while True:
    if command:
        valid_data = re.findall(regex, command)
        if valid_data:
            print(*valid_data,end=' ')
        command = input()
    else:
        break
