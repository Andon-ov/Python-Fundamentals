import sys
from io import StringIO

input1 = """P34562Z q2576f   H456z"""

sys.stdin = StringIO(input1)

text = input().split()
sums = 0

for i in text:

    first_letter = i[0]
    first_letter_number = int(ord(first_letter) & 31)

    last_letter = i[-1]
    last_letter_number = int(ord(last_letter) & 31)

    number = int(i[1:-1])

    if first_letter.isupper():
        # divide the number by the letter's position
        number /= first_letter_number

    else:
        # multiply the number with the letter's position
        number *= first_letter_number

    if last_letter.isupper():
        # subtract its position from the resulting number
        number -= last_letter_number
        sums += number


    else:
        # add its position to the resulting number
        number += last_letter_number
        sums += number

print(f'{sums:.2f}')
