# def exists_item(item,list):
#     if item in list:
#         return True
#     return False
#
#
# shopping_list = input().split('!')
# command = input()
#
# while not command == 'Go Shopping!':
#     command = command.split()
#     action = command[0]
#     item = command[1]
#     if action == 'Urgent':
#         if not exists_item(item,shopping_list):
#             shopping_list.insert(0,item)
#     elif action == 'Unnecessary':
#         if exists_item(item,shopping_list):
#             shopping_list.remove(item)
#     elif action == 'Correct':
#         new_item = command[2]
#         if exists_item(item,shopping_list):
#             old_item = shopping_list.index(item)
#             shopping_list[old_item] = new_item
#     elif action == 'Rearrange':
#         if exists_item(item,shopping_list):
#             remouved_item = shopping_list.index(item)
#             replace_item = shopping_list.pop(remouved_item)
#             shopping_list.append(replace_item)
#
#     command = input()
# print(", ".join(shopping_list))

def item_exists(list, item):
    if item in list:
        return True
    return False

shopping_list = input().split("!")
command = input()
while not command == "Go Shopping!":
    command_split = command.split()
    action = command_split[0]
    item = command_split[1]
    if action == 'Urgent':
        if not item_exists(shopping_list,item):
            shopping_list.insert(0,item)

    elif action == 'Unnecessary':
        if item_exists(shopping_list,item):
            shopping_list.remove(item)

    elif action == 'Correct':
        new_item = command_split[2]
        if item_exists(shopping_list, item):
            index = shopping_list.index(item)
            shopping_list[index] = new_item

    elif action == 'Rearrange':
        if item_exists(shopping_list, item):
            index = shopping_list.index(item)
            shopping_list.append(shopping_list.pop(index))

    command = input()

print(", ".join(shopping_list))














