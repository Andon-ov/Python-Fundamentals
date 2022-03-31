# https://pythex.org/
# https://regex101.com/
# https://regexr.com/

# import re
#
# pattern = r"((www)\.([A-Za-z0-9]+([\-[A-Za-z0-9]+)*(\.[a-z]+)+))"
#
#
# data = input()
# while data:
#
#     matches = re.finditer(pattern, data)
#     for match in matches:
#         print(match.group())
#
#     data = input()
#

import re

regex = r"((www)\.([A-Za-z0-9]+([\-[A-Za-z0-9]+)*(\.[a-z]+)+))"
text = input()
while True:

    matches = re.findall(regex, text)
    if matches:
        for url in matches:
            print(url[0])
    elif text == '':
        break

    text = input()

