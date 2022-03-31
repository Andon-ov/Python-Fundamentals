# def index_in_range(index,len):
#     if index in range(len):
#         return True
#     return False
#
#
# targets =[int(i) for i in input().split()]
# command = input()
# while not command == 'End':
#
#     action,index,power = command.split()
#     index = int(index)
#     power = int(power)
#
#     if action == 'Shoot':
#         if index_in_range(index, len(targets)):
#             targets[index] -= power
#             if targets[index] <= 0:
#                 targets.pop(index)
#
#     elif action == 'Add':
#         if index_in_range(index, len(targets)):
#             targets.insert(index,power)
#
#         else:
#             print('Invalid placement!')
#
#     elif action == 'Strike':
#         el1 = (index - power)
#         el2 = (index + power) + 1
#
#         if index_in_range(index, len(targets)) and\
#                 index_in_range(el1,len(targets)) and\
#                 index_in_range(el2,len(targets)):
#             del targets[el1:el2]
#
#         else:
#             print("Strike missed!")
#
#     command = input()
# print('|'.join([str(i) for i in targets]))


targets = [int(x) for x in input().split()]

command = input()
while not command == "End":
    command_split = command.split()
    action = command_split[0]
    index = int(command_split[1])
    value = int(command_split[2])

    if action == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif action == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, value)

        else:
            print("Invalid placement!")

    elif action == 'Strike':
        if 0 <= index < len(targets) and 0 <= index + value < len(targets) and 0 <= index - value < len(targets):

            start_target = targets[:index - value]
            end_target = targets[index + value + 1:]
            targets = start_target + end_target

        else:
            print("Strike missed!")

    command = input()

print('|'.join([str(x) for x in targets]))
