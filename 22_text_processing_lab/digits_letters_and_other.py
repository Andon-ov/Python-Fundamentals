# digits = ''
# letters = ''
# other = ''
#
# text = input()
# for char in text:
#     if char.isdigit():
#         digits += char
#     elif char.isalpha():
#         letters += char
#     else:
#         other += char
# print(digits)
# print(letters)
# print(other)


import sys
from io import StringIO

input1 = """Agd#53Dfg^&4F53"""

sys.stdin = StringIO(input1)
is_alpha = ''
is_digit = ''
other = ''
text = input()
for i in text:
    if i.isalpha():
        is_alpha += i
    elif i.isdigit():
        is_digit += i
    else:
        other += i

print(is_digit)
print(is_alpha)
print(other)
