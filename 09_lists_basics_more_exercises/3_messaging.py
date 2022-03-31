# def secret_index(list):
#     index = []
#     sums = 0
#     for number in list:
#         for digit in number:
#             sums += int(digit)
#         index.append(sums)
#         sums = 0
#     return index
#
#
# code = input().split()
# message = list(input())
# secret_message = []
#
# for number in (secret_index(code)):
#
#     if number > len(message):
#         number -= len(message)
#
#     print(message.pop(number),end='')
#

def number_to_index(numbers_as_a_string):
    searched_index = []
    for i in numbers_as_a_string:
        number = 0
        for j in i:
            number += int(j)
        searched_index.append(number)
    return searched_index


numbers = number_to_index(input().split())
string = list(input())

for number in numbers:
    if number > len(string):
        number -= len(string)
    print(string.pop(number),end='')

















