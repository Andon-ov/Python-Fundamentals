import sys
from io import StringIO

input1 = """aaaaabbbbbcdddeeeedssaa"""

sys.stdin = StringIO(input1)

text = input()
new_text = ''

for i in range(len(text)-1):

    if not text[i] == text[i+1]:
        new_text += text[i]
new_text += text[-1]

print(new_text)



# data = input()
# index = 0
# # започаме със стартиращ индекс 0
# while index < len(data)-1:
#     # ако има 2 еднакви букви
#     if data[index] == data[index+1]:
#         # създаваме пеоменлива с тях
#         element_to_replace = f'{data[index]}{data[index+1]}'
#         # реплейсваме в текста двете еднакви букви с една
#         data = data.replace(element_to_replace,data[index])
#         # и започваме пак от начало
#         index = 0
#     else:
#         # ако няма какво да реплейсваме овеличаваме брояча докато се изръвни с дължината на текста
#         index += 1
# print(data)








