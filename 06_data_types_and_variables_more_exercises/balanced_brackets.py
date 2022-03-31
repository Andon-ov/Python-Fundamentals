# bracket = []
# is_balanced = False
#
# n = int(input())
# for _ in range(n):
#     string = input()
#     # Правим лист в който вкарваме само скобите за да може да ги достъпваме по индекс
#     if string in ('(' ')'):
#         bracket.append(string)
#
# for index in range(len(bracket)):
#     # Като прескачаме всеки втори индекс защото сме го достъпили в предната проверка
#     if index % 2 != 0:
#         continue
#     # Правим проверка да линекса не е последния за да не излезем от и листа
#     if index < len(bracket) - 1:
#         # Въртим листа от първата позиция и проверяваме първата и втората позиция дали са равни на съответните скоби
#         if bracket[index] == '(' and bracket[index + 1] == ')':
#             # Ако всичко е наред = True
#             is_balanced = True
#
#         else:
#             is_balanced = False
#
# if is_balanced:
#     print('BALANCED')
# else:
#     print('UNBALANCED')



text = int(input())

balanced = True
open_bracket = False

for _ in range(text):
    string = input()

    if string != '(' and string != ')':
        continue

    is_open_bracket = string == '('

    if open_bracket == is_open_bracket:
        balanced = False
        break

    open_bracket = is_open_bracket

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

