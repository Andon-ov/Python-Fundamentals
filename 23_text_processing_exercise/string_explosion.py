#
# line = input()
# # вход
# total_strength = 0
# # сила на взрива
# i=0
# # променлива за интериране през цикала
# while i < len(line):
#     # взимаме първия символ
#     ch = line[i]
#     # проверяваме да ли не е това което търсим
#     if ch == '>':
#         # ако е взимаме силата на взрива
#         strength = int(line[i+1])
#         # и я довабяме към общата сила
#         total_strength += strength
#     else:
#         # ако сме събрали сила
#         if total_strength > 0:
#             # режим текста със слайсинг
#             line = line[:i] +line[i+1:]
#             # махаме един символ
#             i -= 1
#             # и връщаме една интерация назад
#             total_strength -= 1
#              # вадим от общата сила едно защото сме отрязли замо 1 буква и въртим на ново
#     i +=1
# print(line)
#


# final_text =[]
# text = list(''.join(input()))
#
# munus_len = 0
# for i in text:
#     if i.isdigit():
#         munus_len += int(i)-1
# for i in range(len(text)-munus_len):
#     if not text[i].isdigit():
#         final_text.append(text[i])
#     else:
#         number = int(text[i])
#         for num in range(number-1):
#             text.pop(i)
#
# print(''.join(final_text))



import sys
from io import StringIO

input1 = """abv>1>1>2>2asdasd"""

sys.stdin = StringIO(input1)


string = input()
new_string = ''
power = 0
for i in range(len(string)):

    if string[i] == ">":
        new_string += ">"
        power += int(string[i+1])

    else:
        if power > 0:
            power -= 1
        else:
            new_string += string[i]

print(new_string)











