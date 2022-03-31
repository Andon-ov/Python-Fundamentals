# import re
# pattern = r"(?P<Day>\d{2})(?P<separator>[-/\.])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"
# # https://pythex.org/
# text = input()
# valid_data = re.finditer(pattern,text)
# for data in valid_data:
#     current_date = data.groupdict()
#     print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}", )

import re

text = input()
regex = r"(?P<Day>\d{2})(?P<separator>[-/\.])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"
valid_data = re.finditer(regex, text)
for d in valid_data:
    current_date = d.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}", )
