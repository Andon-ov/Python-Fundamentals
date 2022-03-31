# import re
# pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
# # https://pythex.org/
# text = input()
# valid_numbers = re.finditer(pattern,text)
# valid_numbers = [num.group() for num in valid_numbers]
# print(*valid_numbers)



import re
numbers = input()
regex = r'(^|(?<=\s))-?\d*\.?\d+($|(?=\s))'
matches = re.finditer(regex,numbers)
if matches:
    for i in matches:
        print(i.group(0),end=" ")