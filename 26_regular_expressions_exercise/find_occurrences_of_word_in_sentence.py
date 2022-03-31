# import re
# # https://pythex.org/
#
# text = input()
# searched_word = input()
# pattern = rf"\b{searched_word}\b"
#
# valid_text = re.findall(pattern,text,flags=re.I)
# print(len(valid_text))

import re

text = input()
word = input()
regex = f"\\b{word}\\b"
matches = re.findall(regex, text,flags=re.I)
print(len(matches))



















