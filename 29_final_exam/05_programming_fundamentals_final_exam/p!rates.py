# import sys
# from io import StringIO
#
# input1 = """Nassau||95000||1000
# San Juan||930000||1250
# Campeche||270000||690
# Port Royal||320000||1000
# Port Royal||100000||2000
# Sail
# Prosper=>Port Royal=>-200
# Plunder=>Nassau=>94000=>750
# Plunder=>Nassau=>1000=>150
# Plunder=>Campeche=>150000=>690
# End
# """
#
# sys.stdin = StringIO(input1)
#
#
# def add_to_dict(targeted: dict, command):
#     command_split = command.split("||")
#
#     town = command_split[0]
#     population = int(command_split[1])
#     gold = int(command_split[2])
#
#     if town not in targeted:
#         targeted[town] = [population, gold]
#     else:
#         targeted[town][0] += population
#         targeted[town][1] += gold
#
#     return targeted
#
#
# targeted = {}
#
# command = input()
# while not command == "Sail":
#     add_to_dict(targeted, command)
#
#     command = input()
# data = input()
# while not data == "End":
#
#     split_data = data.split("=>")
#     action = split_data[0]
#     town = split_data[1]
#
#     if action == "Plunder":
#         people = split_data[2]
#         gold = split_data[3]
#
#         # if targeted[town][0] - int(people) > 0 and targeted[town][1] - int(gold) >0:
#         targeted[town][0] -= int(people)
#         targeted[town][1] -= int(gold)
#         print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
#         if targeted[town][0] <= 0 or targeted[town][1] <= 0:
#             print(f"{town} has been wiped off the map!")
#             del targeted[town]
#
#     elif action == "Prosper":
#         gold = int(split_data[2])
#         if gold > 0:
#             targeted[town][1] += int(gold)
#             print(f"{gold} gold added to the city treasury. {town} now has {targeted[town][1]} gold.")
#         else:
#             print("Gold added cannot be a negative number!")
#
#     data = input()
# print(f"Ahoy, Captain! There are {len(targeted)} wealthy settlements to go to:")
# for key, value in targeted.items():
#     print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")


import sys
from io import StringIO

input1 = """Tortuga||345000||1250
Santo Domingo||240000||630
Havana||410000||1100
Sail
Plunder=>Tortuga=>75000=>380
Prosper=>Santo Domingo=>180
End"""
input2 = """Nassau||95000||1000
San Juan||930000||1250
Campeche||270000||690
Port Royal||320000||1000
Port Royal||100000||2000
Sail
Prosper=>Port Royal=>-200
Plunder=>Nassau=>94000=>750
Plunder=>Nassau=>1000=>150
Plunder=>Campeche=>150000=>690
End"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

targeted_cities = {}
command = input()
while not command == "Sail":
    command_split = command.split("||")
    cities = command_split[0]
    population = int(command_split[1])
    gold = int(command_split[2])
    if cities not in targeted_cities:
        targeted_cities[cities] = [population, gold]
    else:
        targeted_cities[cities][0] += population
        targeted_cities[cities][1] += gold
    command = input()

data = input()
while not data == "End":
    data_split = data.split('=>')
    action = data_split[0]
    town = data_split[1]
    if action == "Plunder":
        people = int(data_split[2])
        gold = int(data_split[3])
        targeted_cities[town][0] -= people
        targeted_cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if targeted_cities[town][0] <= 0 or targeted_cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del targeted_cities[town]

    else:
        gold = int(data_split[2])
        if gold <= 0:
            print("Gold added cannot be a negative number!")
        else:
            targeted_cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targeted_cities[town][1]} gold.")

    data = input()
if len(targeted_cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for key,value in targeted_cities.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")