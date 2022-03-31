
# array = [int(i) for i in input().split()]
# command = input().split()
# while not command[0] == "end":
#
#     action = command[0]
#     if action == 'swap':
#         first_index = int(command[1])
#         second_index = int(command[2])
#         array[first_index],array[second_index] = array[second_index], array[first_index]
#
#     elif action == 'multiply':
#         first_index = int(command[1])
#         second_index = int(command[2])
#         array[first_index] = array[first_index] * array[second_index]
#
#
#     elif action == 'decrease':
#         for index in range(len(array)):
#             array[index] -= 1
#
#     command = input().split()
#
# print(', '.join([str(i) for i in array] ))


array = [int(x) for x in input().split()]
command = input()
while not command == "end":
    split_command = command.split()
    action = split_command[0]
    if action == 'swap':
        index_one = int(split_command[1])
        index_two = int(split_command[2])
        array[index_one],array[index_two] = array[index_two],array[index_one]

    elif action == 'multiply':
        index_one = int(split_command[1])
        index_two = int(split_command[2])
        array[index_one] *= array[index_two]

    elif action == 'decrease':
        for index in range(len(array)):
            array[index] -= 1

    command = input()

print(', '.join([str(x) for x in array]))










