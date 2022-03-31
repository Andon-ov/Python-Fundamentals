# import re
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# # https://pythex.org/
# text = input()
# valid_names = re.findall(pattern,text)
# print(*valid_names)
# # print(' '.join(valid_names))

import re
names = input()
regex = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
matches = re.findall(regex,names)
if matches:
    print(*matches)




















