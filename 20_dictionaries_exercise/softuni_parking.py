# n = int(input())
# parking = {}
# for _ in range(n):
#     data = input()
#     split_data = data.split()
#     command = split_data[0]
#     name = split_data[1]
#
#     if command == 'register':
#         number = split_data[2]
#
#         if name not in parking:
#             parking[name] = number
#             print(f"{name} registered {number} successfully")
#         elif name in parking:
#             print(f'ERROR: already registered with plate number {number}')
#
#     elif command == 'unregister':
#         if name in parking:
#             parking.pop(name)
#             print(f"{name} unregistered successfully")
#         else:
#             print(f"ERROR: user {name} not found")
# for key,value in parking.items():
#     print(f"{key} => {value}")

def register_car(dict, name, car):
    if name not in dict:
        print(f'{name} registered {car} successfully')
        dict[name] = car
    else:
        print(f"ERROR: already registered with plate number {dict[name]}")
    return dict


def unregister_car(dict, name):
    if name in dict:
        print(f'{name} unregistered successfully')
        del dict[name]
    else:
        print(f'ERROR: user {name} not found')
    return dict


parking = {}
n = int(input())
for _ in range(n):
    command = input().split()
    action = command[0]
    name = command[1]

    if action == 'register':
        car = command[2]
        register_car(parking, name, car)

    elif action == 'unregister':
        unregister_car(parking, name)

for key, value in parking.items():
    print(f"{key} => {value}")
