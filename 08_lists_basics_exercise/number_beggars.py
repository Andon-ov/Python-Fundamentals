# sums_list = input().split(", ")
# number_of_beggars = int(input())
#
# final_list = []
# sums_list_as_digits = []
#
# counter_of_index = 0
# temp_sum = 0
#
# for index in range(len(sums_list)):
#     sums_list_as_digits.append(int(sums_list[index]))
#
# while counter_of_index < number_of_beggars:
#
#     for element in range(counter_of_index, len(sums_list_as_digits), number_of_beggars):
#         temp_sum += sums_list_as_digits[element]
#
#     final_list.append(temp_sum)
#     temp_sum = 0
#     counter_of_index +=1
#
# print(final_list)

money = [int(i) for i in input().split(", ")]
beggars = int(input())

start_index = 0  # Създаваме старт индексът, който започва да брои просяците
sums_of_each_beggars = []  # Тук събираме сумите на просяците

for i in range(beggars):  # Въртим фор цикъл с просяците и на всеки един събираме неговата сума
    current_sum = 0  # Тук сумата започва от нула
    for index in range(start_index, len(money), beggars):  # Въртим фор цикъл от началния индекс до дължината на листа
        # с паричките със стъпка броя на просяците (за да може да има парички за всички)
        current_sum += money[index]  # Събираме сумата на всеки един просяк
    start_index += 1  # Променяме индекса за да може следващия просяк да започне от следващото число
    sums_of_each_beggars.append(current_sum)  # И добавяме събраната сума в листа
print(sums_of_each_beggars)
