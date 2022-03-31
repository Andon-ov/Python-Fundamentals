import sys
from io import StringIO

input1 = """-2, 2, 1, 5, 9, 3, 2, -2, 1, -1, -3, 3
7
expensive"""

sys.stdin = StringIO(input1)


def cheap(cheap_list, number):
    cheap_sum = 0

    for cheap_number in cheap_list:
        if number > cheap_number:
            cheap_sum += cheap_number

    return cheap_sum


def expensive(expensive_list, number):
    expensive_sum = 0

    for expensive_number in expensive_list:
        if number <= expensive_number:
            expensive_sum += expensive_number

    return expensive_sum


price_rating = [int(x) for x in input().split(", ")]
index = int(input())
type_of_item = input()

entry_pint = price_rating[index]
left_part = price_rating[:index]
right_part = price_rating[index + 1:]

left_sum = 0
right_sum = 0

if type_of_item == 'cheap':
    left_sum = cheap(left_part, entry_pint)
    right_sum = cheap(right_part, entry_pint)

elif type_of_item == "expensive":
    left_sum = expensive(left_part, entry_pint)
    right_sum = expensive(right_part, entry_pint)

if left_sum > right_sum:
    print(f"Left - {left_sum}")
elif left_sum < right_sum:
    print(f"Right - {right_sum}")
elif left_sum == right_sum:
    print(f"Left - {left_sum}")



# Всеки предмет си има цена числата показват колко струва всеки предмет за собственика на Джон.
# Ние ще получим входяща точка оттам от, където Джон ще започне да чупи, предмети първо на негово ляво после на негово дясно.
# Джон никога няма да счупи предмета на входната точка. Трябва да пресметнем щетите,
# който Джон нанася на неговата лява и на неговата дясна страна. И да принтираме само по-голямото число.
# Ако двете суми са равни принтираме, че е лявата страна!!!
# На третия ред получаваме видът предметите, които Джон иска да счупи:
# Евтини - предмети, които имат по-ниска цена  от входящата точка.
# Скъпи предмети - които имат равна или по-висока цена от входящата точка.
