# day_events_list = input().split("|")
#
# MAX_ENERGY = 100
# ORDER_ENERGY = 30
# REST_ENERGY = 50
# energy = 100
# coins = 100
# is_not_bankrupt = True
#
# for event in day_events_list:
#
#     single_events_list = event.split("-")
#     name = single_events_list[0]
#     value = int(single_events_list[1])
#
#     if name == "rest":
#         gained_energy = 0
#
#         if energy + value > MAX_ENERGY:
#             gained_energy = MAX_ENERGY - energy
#             energy = MAX_ENERGY
#         else:
#             energy += value
#             gained_energy = value
#
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {energy}.")
#
#     elif name == "order":
#         if energy >= ORDER_ENERGY:
#             energy -= ORDER_ENERGY
#             coins += value
#             print(f"You earned {value} coins.")
#         else:
#             energy += REST_ENERGY
#             print("You had to rest!")
#             continue
#
#     else:
#         if coins > value:
#             coins -= value
#             print(f"You bought {name}.")
#         else:
#             print(f"Closed! Cannot afford {name}.")
#             is_not_bankrupt = False
#             break
#
# if is_not_bankrupt:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {energy}")


energy = 100
coins = 100
events = input().split('|')
for i in events:
    command = i.split('-')
    action = command[0]
    value = int(command[1])

    if action == "rest":

        if energy >= 100:
            energy = 100
            print(f"You gained {energy-100} energy.")

        elif energy + value <= 100:
            energy += value
            print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")

    elif action == "order":
        if energy >= 30:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins > value:
            print(f"You bought {action}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {action}.")
            exit()

print(f"Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
