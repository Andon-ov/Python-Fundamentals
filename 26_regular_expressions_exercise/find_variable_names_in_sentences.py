# import re
# pattern = r"\b_([A-Za-z0-9]+)\b"
# # https://pythex.org/
#
# text = input()
#
# valid_text = re.findall(pattern, text)
# if valid_text:
#     print(','.join(valid_text),end=' ')


import re
text = input()
matches = re.findall(r"\b_([A-Za-z0-9]+)\b", text)
print(','.join(matches))




