# import re
# pattern = r"((\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4}))\b"
# # https://pythex.org/
# text = input()
# valid_numbers = re.finditer(pattern,text)
# valid_phones = [i.group() for i in valid_numbers]
# print(', '.join(valid_phones))


import re
numbers = input()
regex = r'\+359\s2\s\d{3}\s\d{4}|\+359\-2\-\d{3}\-\d{4}\b'
matches = re.findall(regex,numbers)
if matches:
    print(", ".join(matches))



















