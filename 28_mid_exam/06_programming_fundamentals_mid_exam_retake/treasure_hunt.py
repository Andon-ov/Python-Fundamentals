# treasure_chest = input().split('|')
#
# command = input()
# while not command == "Yohoho!":
#     command_args = command.split()
#     action = command_args[0]
#
#     if action == 'Loot':
#         items = command_args[1:]
#         for item in items:
#             if item not in treasure_chest:
#                 treasure_chest.insert(0, item)
#
#     elif action == 'Drop':
#         index = int(command_args[1])
#         if index < 0 or index >= len(treasure_chest):
#             command = input()
#             continue
#         removed_item = treasure_chest.pop(index)
#         treasure_chest.append(removed_item)
#
#     elif action == 'Steal':
#         count = int(command_args[1])
#         removed_item = treasure_chest[-count:]
#         print(', '.join(removed_item))
#         treasure_chest = treasure_chest[:-count]
#
#     command = input()
#
# if len(treasure_chest) == 0:
#     print('Failed treasure hunt.')
# else:
#     all_char = 0
#     for i in treasure_chest:
#         all_char += len(i)
#     print(f'Average treasure gain: {(all_char / len(treasure_chest)):.2f} pirate credits.')
#


treasure_chest = input().split("|")
command = input()
while not command == "Yohoho!":

    command_split = command.split()
    action = command_split[0]

    if action == 'Loot':
        items = command_split[1:]
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif action == 'Drop':
        index = int(command_split[1])
        if 0 <= index < len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(index))

    elif action == 'Steal':
        index = int(command_split[1])
        steal_items = treasure_chest[- index:]
        print(', '.join(steal_items))
        treasure_chest = treasure_chest[:- index]

    command = input()

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = 0
    for i in treasure_chest:
        average_treasure_gain += len(i)
    print(f"Average treasure gain: {average_treasure_gain / len(treasure_chest):.2f} pirate credits.")
