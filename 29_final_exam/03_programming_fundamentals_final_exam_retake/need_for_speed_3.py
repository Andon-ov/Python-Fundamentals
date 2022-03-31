# import sys
# from io import StringIO
#
# input1 = """3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000
# Stop
# """
# input2 = """4
# Lamborghini Veneno|11111|74
# Bugatti Veyron|12345|67
# Koenigsegg CCXR|67890|12
# Aston Martin Valkryie|99900|50
# Drive : Koenigsegg CCXR : 382 : 82
# Drive : Aston Martin Valkryie : 99 : 23
# Drive : Aston Martin Valkryie : 2 : 1
# Refuel : Lamborghini Veneno : 40
# Revert : Bugatti Veyron : 2000
# Stop
# """
# sys.stdin = StringIO(input1)
#
# possession = {}
# n = int(input())
# for _ in range(n):
#     data = input().split("|")
#     car = data[0]
#     mileage = int(data[1])
#     fuel = int(data[2])
#     if car not in possession:
#         possession[car] = []
#     possession[car].append(mileage)
#     possession[car].append(fuel)
#
# command = input()
# while not command == "Stop":
#     command_split = command.split(" : ")
#     action = command_split[0]
#     car = command_split[1]
#
#     if action == "Drive":
#         distance = int(command_split[2])
#         fuel = int(command_split[3])
#         if fuel > possession[car][1]:
#             print("Not enough fuel to make that ride")
#         else:
#             print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#             possession[car][1] -= fuel
#             possession[car][0] += distance
#             if possession[car][0] >= 100000:
#                 print(f"Time to sell the {car}!")
#                 del possession[car]
#
#     elif action == "Refuel":
#         fuel = int(command_split[2])
#         max_fuel = 75
#         if possession[car][1] + fuel <= max_fuel:
#             print(f"{car} refueled with {fuel} liters")
#             possession[car][1] += fuel
#
#         else:
#             print(f"{car} refueled with {max_fuel - possession[car][1]} liters")
#             possession[car][1] = 75
#
#     elif action == "Revert":
#         kilometers = int(command_split[2])
#         if possession[car][0] - kilometers > 10000:
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#             possession[car][0] -= kilometers
#
#         else:
#             possession[car][0] -= kilometers
#             if possession[car][0] <= 10000:
#                 possession[car][0] = 10000
#
#     command = input()
#
# sorted_possession = sorted(possession.items(), key=lambda kv: (-kv[1][0], kv[0]))
#
# for i in sorted_possession:
#
#     print(f"{i[0]} -> Mileage: {i[1][0]} kms, Fuel in the tank: {i[1][1]} lt.")

import sys
from io import StringIO

input1 = """3
Audi A6|38000|62
Mercedes CLS|11000|35
Volkswagen Passat CC|45678|5
Drive : Audi A6 : 543 : 47
Drive : Mercedes CLS : 94 : 11
Drive : Volkswagen Passat CC : 69 : 8
Refuel : Audi A6 : 50
Revert : Mercedes CLS : 500
Revert : Audi A6 : 30000
Stop
"""
input2 = """4
Lamborghini Veneno|11111|74
Bugatti Veyron|12345|67
Koenigsegg CCXR|67890|12
Aston Martin Valkryie|99900|50
Drive : Koenigsegg CCXR : 382 : 82
Drive : Aston Martin Valkryie : 99 : 23
Drive : Aston Martin Valkryie : 2 : 1
Refuel : Lamborghini Veneno : 40
Revert : Bugatti Veyron : 2000
Stop
"""
input3 = """"""

sys.stdin = StringIO(input2)

need_for_speed = {}
n = int(input())

for i in range(n):
    car, mileage, fuel = input().split("|")
    need_for_speed[car] = [int(mileage),int(fuel)]

command = input()
while not command == "Stop":
    command_split = command.split(" : ")
    action = command_split[0]
    car = command_split[1]

    if action == "Drive":

        distance = int(command_split[2])
        fuel = int(command_split[3])

        if fuel <= need_for_speed[car][1]:
            need_for_speed[car][0] += distance
            need_for_speed[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if need_for_speed[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del need_for_speed[car]
        else:
            print("Not enough fuel to make that ride")

    elif action == "Refuel":
        fuel = int(command_split[2])
        if need_for_speed[car][1] + fuel <= 75:
            need_for_speed[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            add_fuel = 75 - need_for_speed[car][1]
            print(f"{car} refueled with {add_fuel} liters")
            need_for_speed[car][1] += add_fuel

    elif action == "Revert":
        kilometers = int(command_split[2])
        need_for_speed[car][0] -= kilometers

        if need_for_speed[car][0]< 10000:
            need_for_speed[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for key, value in need_for_speed.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")