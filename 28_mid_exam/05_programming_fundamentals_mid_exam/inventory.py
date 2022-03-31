# inventory = input().split(", ")
#
# command = input()
# while not command == "Craft!":
#     command_split = command.split(" - ")
#     action = command_split[0]
#
#     if action == "Collect":
#         item = command_split[1]
#         if item not in inventory:
#             inventory.append(item)
#
#     elif action == "Drop":
#         item = command_split[1]
#         if item in inventory:
#             inventory.remove(item)
#
#     elif action == "Combine Items":
#         old_item, new_item = command_split[1].split(':')
#         if old_item in inventory:
#             for index, value in enumerate(inventory):
#                 if value == old_item:
#                     new_index = index + 1
#                     inventory.insert(new_index, new_item)
#
#     elif action == "Renew":
#         item = command_split[1]
#         if item in inventory:
#             inventory.remove(item)
#             inventory.append(item)
#
#     command = input()
#
# for item in inventory:
#     print(', '.join(inventory))
#     exit()

def if_not_exist(list, item):
    if item not in list:
        return True
    else:
        return False


journal = input().split(", ")
command = input()
while not command == "Craft!":
    command_split = command.split(" - ")
    action = command_split[0]

    if action == "Collect":
        item = command_split[1]
        if if_not_exist(journal, item):
            journal.append(item)

    if action == "Drop":
        item = command_split[1]
        if not if_not_exist(journal, item):
            journal.remove(item)

    if action == "Combine Items":
        items = command_split[1].split(":")
        item = items[0]
        new_item = items[1]
        if not if_not_exist(journal, item):
            index = journal.index(item)
            journal.insert(index+1, new_item)

    if action == "Renew":
        item = command_split[1]
        if not if_not_exist(journal, item):
            journal.remove(item)
            journal.append(item)

    command = input()
print(', '.join([x for x in journal]))