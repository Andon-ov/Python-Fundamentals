import sys
from io import StringIO

input1 = """aSd22&5s@1"""

sys.stdin = StringIO(input1)

new_string = []
text = input()
string = ''
number = ''

for i in text:
    if i.isdigit():
        number += i

    else:
        while not number == "":
            new_string.append(string.upper()*int(number))
            number = ''
            string = ''
        string += i

new_string.append(string.upper() * int(number))

print(f'Unique symbols used: {len(set("".join(new_string)))}')
print(''.join(new_string))
