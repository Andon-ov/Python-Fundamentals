# import re
# pattern = r"((?<=\s)([a-z0-9]+[-\.\_a-z0-9]*)@([a-z]+)(-[a-z]+)*\.([a-z\.]+))\b"
# # https://pythex.org/
# # https://regex101.com/
# text = input()
#
# valid_text = re.findall(pattern, text)
# if valid_text:
#     for mail in valid_text:
#         print(mail[0])


import re

text = input()

regex = r"(?<=\s)[a-z0-9]+[-\.\_a-z0-9]*@[a-z0-9]+[-\.a-z]*\.[a-z]+"
matches = re.finditer(regex, text)
for i in matches:
    print(i.group(0))




















