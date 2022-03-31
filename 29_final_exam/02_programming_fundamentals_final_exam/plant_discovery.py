#
# import sys
# from io import StringIO
#
# input1 = """3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition
# """
# input2 = """2
# Candelabra<->10
# Oahu<->10
# Exhibition"""
# input3 = """"""
#
# sys.stdin = StringIO(input1)

# plants_rarity = {}
# plants_rating = {}
#
# n = int(input())
# for i in range(n):
#     data = input().split("<->")
#
#     plant = data[0]
#     rarity = data[1]
#     plants_rarity[plant] = rarity
#
# command = input()
# while not command == "Exhibition":
#     command_split = command.split(": ")
#     action = command_split[0]
#
#     if action == "Rate":
#         split_command = command_split[1].split(" - ")
#         plant = split_command[0]
#         rating = int(split_command[1])
#
#         if plant in plants_rarity:
#             if plant not in plants_rating:
#                 plants_rating[plant] = []
#             plants_rating[plant].append(rating)
#         else:
#             print("error")
#
#     elif action == "Update":
#         split_command = command_split[1].split(" - ")
#         plant = split_command[0]
#         new_rarity = int(split_command[1])
#         if plant in plants_rarity:
#             plants_rarity[plant] = new_rarity
#         else:
#             print("error")
#
#     elif action == "Reset":
#         plant = command_split[1]
#         if plant in plants_rating:
#             del plants_rating[plant]
#
#         else:
#             print("error")
#
#     command = input()
#
# print("Plants for the exhibition:")
# for key, value in plants_rarity.items():
#     # plants_and_rarity = sorted(plants_and_rarity.items(), key=lambda kv: -kv[1]) - ако се сортира
#     if len(plants_rating) == 0:
#         rate = 0
#         print(f"- {key}; Rarity: {value}; Rating: {rate:.2f}")
#
#     elif key not in plants_rating:
#         rate = 0
#         print(f"- {key}; Rarity: {value}; Rating: {rate:.2f}")
#
#     else:
#         rate = sum(plants_rating[key])/len(plants_rating[key])
#
#         print(f"- {key}; Rarity: {value}; Rating: {rate:.2f}")


# Решена с Клас
# class Plant:
#     def __init__(self, name, rarity):
#         self.name = name
#         self.rarity = rarity
#         self.ratings = []
#
#     def rating(self):
#         if self.ratings:
#             return sum(self.ratings) / len(self.ratings)
#         return 0
#
#
# plants = {}
#
# n = int(input())
# for num in range(n):
#     token = input().split('<->')
#     plant_name = token[0]
#     plant_rarity = token[1]
#     plants[plant_name] = Plant(plant_name, int(plant_rarity))
#
# command = input()
# while command != 'Exhibition':
#     token_2 = command.split(': ')
#     token_3 = token_2[1].split(' - ')
#     plant_name = token_3[0]
#     command_type = token_2[0]
#
#     if plant_name not in plants:
#         print('error')
#
#     elif command_type == 'Rate':
#         rating = token_3[1]
#         plants[plant_name].ratings.append(int(rating))
#
#     elif command_type == 'Update':
#         new_rarity = int(token_3[1])
#         plants[plant_name].rarity = new_rarity
#
#     elif command_type == 'Reset':
#         plants[plant_name].ratings.clear()
#
#     else:
#         print('error')
#
#     command = input()
#
# print(f'Plants for the exhibition:')
# for plant in plants.values():
#     print(f'- {plant.name}; Rarity: {plant.rarity}; Rating: {plant.rating():.2f}')


# num = int(input())
# plants = {}
# for i in range(num):
#     command = input().split("<->")
#     plant = command[0]
#     rarity = int(command[1])
#
#     plants[plant] = []
#     plants[plant].append(rarity)


# while True:
#     command = input()
#     if command == "Exhibition":
#         break
#     current_command = command.split(": ")[0]
#     second_part = command.split(": ")[1]
#     if "Rate" in command:
#         plant_to_be_rated = second_part.split(" - ")[0]
#         rating_plant = int(second_part.split(" - ")[1])
#         if plant_to_be_rated not in plants.keys():
#             print("error")
#         else:
#             plants[plant_to_be_rated].append(rating_plant)
#     elif "Update" in command:
#         plant_tobe_updated = second_part.split(" - ")[0]
#         if plant_tobe_updated not in plants.keys():
#             print("error")
#         else:
#             new_rarity = int(second_part.split(" - ")[1])
#             plants[plant_tobe_updated].pop(0)
#             plants[plant_tobe_updated].insert(0, new_rarity)
#     elif "Reset" in command:
#         plant_to_be_reset = command.split(": ")[1]
#         if plant_to_be_reset not in plants.keys():
#             print("error")
#         else:
#             rarity_to_add_back = plants[plant_to_be_reset][0]
#             plants[plant_to_be_reset].clear()
#             plants[plant_to_be_reset].append(rarity_to_add_back)
#             # plants[plant_to_be_reset].insert(1, 0)
#     else:
#         print("error")
#
# for key, value in plants.items():
#     item_to_amend = value[1:]
#     remaining_part = value[0]
#     if len(item_to_amend) > 1:
#         total = sum(item_to_amend)
#         new_num = total / len(item_to_amend)
#         value.clear()
#         value.append(remaining_part)
#         value.append(new_num)
#     if len(value) == 1:
#         value.append(0)
#
# print(f"Plants for the exhibition:")
# plants = dict(sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])))
# for key, value in plants.items():
#     print(f"- {key}; Rarity: {int(value[0])}; Rating: {value[1]:.2f}")

import sys
from io import StringIO

input1 = """3
Arnoldii<->4
Woodii<->7
Welwitschia<->2
Rate: Woodii - 10
Rate: Welwitschia - 7
Rate: Arnoldii - 3
Rate: Woodii - 5
Update: Woodii - 5
Reset: Arnoldii
Exhibition
"""
input2 = """2
Candelabra<->10
Oahu<->10
Exhibition"""
input3 = """"""

sys.stdin = StringIO(input1)

n = int(input())
plants = {}
for _ in range(n):
    data = input()
    data_split = data.split("<->")
    plant = data_split[0]
    rarity = int(data_split[1])
    if plant not in plants:
        plants[plant] = []
    plants[plant] = [rarity]

command = input()
while not command == "Exhibition":
    command_split = command.split(': ')
    action = command_split[0]
    if action == "Rate":
        second_command_split = command_split[1].split(" - ")
        plant = second_command_split[0]
        rating = int(second_command_split[1])
        plants[plant].append(rating)

    elif action == "Update":
        second_command_split = command_split[1].split(" - ")
        plant = second_command_split[0]
        new_rarity = int(second_command_split[1])
        plants[plant].insert(new_rarity, 0)
        plants[plant].pop(1)

    elif action == "Reset":
        second_command_split = command_split[1].split(" - ")
        plant = second_command_split[0]
        plants[plant] = plants[plant][:1]

    command = input()
print(plants)
