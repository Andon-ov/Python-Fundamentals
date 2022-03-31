
# neighborhood = [int(i) for i in input().split("@")]
# position = 0
# commands = input()
# while not commands == 'Love!':
#
#     commands = commands.split()
#     lenght_jump = int(commands[1])
#
#     position = position + lenght_jump
#
#     if position >= len(neighborhood):
#         position = 0
#
#     if neighborhood[position] == 0:
#         print(f"Place {position} already had Valentine's day.")
#
#     else:
#         neighborhood[position] -= 2
#
#         if neighborhood[position] == 0:
#             print(f"Place {position} has Valentine's day.")
#
#     commands = input()
# print(f"Cupid's last position was {position}.")
# if neighborhood.count(0)< len(neighborhood):
#     print(f'Cupid has failed {len(neighborhood)-neighborhood.count(0)} places.')
# else:
#     print(f"Mission was successful.")


#
string = [int(x) for x in input().split("@")]
command = input()
last_position_index = 0

while not command == "Love!":

    split_command = command.split()
    jump = int(split_command[1])
    last_position_index = last_position_index + jump

    if last_position_index > len(string) - 1:
        last_position_index = 0

    if string[last_position_index] == 0:
        print(f"Place {last_position_index} already had Valentine's day.")

    if string[last_position_index] >= 2:
        string[last_position_index] -= 2

        if string[last_position_index] <= 0:
            print(f"Place {last_position_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {last_position_index}.")
if string.count(0) < len(string):
    print(f"Cupid has failed {len(string)-string.count(0)} places.")
elif string.count(0) == len(string):
    print("Mission was successful.")