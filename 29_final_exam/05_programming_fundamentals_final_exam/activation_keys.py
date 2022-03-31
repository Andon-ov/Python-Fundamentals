# import sys
# from io import StringIO
#
# input1 = """abcdefghijklmnopqrstuvwxyz
# Slice>>>2>>>6
# Flip>>>Upper>>>3>>>14
# Flip>>>Lower>>>5>>>7
# Contains>>>def
# Contains>>>deF
# Generate
# """
#
# sys.stdin = StringIO(input1)
#
# activation_key = input()
# command = input()
# while not command == "Generate":
#     command_split = command.split(">>>")
#     action = command_split[0]
#
#     if action == "Contains":
#         substring = command_split[1]
#         if substring in activation_key:
#             print(f"{activation_key} contains {substring}")
#         else:
#             print("Substring not found!")
#
#     elif action == "Flip":
#         upper_or_lower = command_split[1]
#         start_index = int(command_split[2])
#         end_index = int(command_split[3])
#
#         if upper_or_lower == "Upper":
#             left_part = activation_key[:start_index]
#             middle_part = activation_key[start_index:end_index].upper()
#             right_part = activation_key[end_index:]
#             activation_key = left_part + middle_part + right_part
#         else:
#             left_part = activation_key[:start_index]
#             middle_part = activation_key[start_index:end_index].lower()
#             right_part = activation_key[end_index:]
#             activation_key = left_part + middle_part + right_part
#         print(activation_key)
#
#     elif action == "Slice":
#         start_index = int(command_split[1])
#         end_index = int(command_split[2])
#
#         left_part = activation_key[:start_index]
#         right_part = activation_key[end_index:]
#         activation_key = left_part + right_part
#         print(activation_key)
#
#     command = input()
# print(f"Your activation key is: {activation_key}")


import sys
from io import StringIO

input1 = """abcdefghijklmnopqrstuvwxyz
Slice>>>2>>>6
Flip>>>Upper>>>3>>>14
Flip>>>Lower>>>5>>>7
Contains>>>def
Contains>>>deF
Generate"""

input2 = """134softsf5ftuni2020rockz42
Slice>>>3>>>7
Contains>>>-rock
Contains>>>-uni-
Contains>>>-rocks
Flip>>>Upper>>>2>>>8
Flip>>>Lower>>>5>>>11
Generate"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

raw_activation_key = input()
command = input()
while not command == "Generate":
    command_split = command.split(">>>")
    action = command_split[0]

    if action == "Contains":
        substring = command_split[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        upper_or_lower = command_split[1]
        start_index = int(command_split[2])
        end_index = int(command_split[3])
        left_part = raw_activation_key[:start_index]
        middle_part = raw_activation_key[start_index:end_index]
        right_part = raw_activation_key[end_index:]
        if upper_or_lower == "Upper":
            middle_part = middle_part.upper()
            raw_activation_key = left_part + middle_part + right_part
            print(raw_activation_key)
        else:
            middle_part = middle_part.lower()
            raw_activation_key = left_part + middle_part + right_part
            print(raw_activation_key)

    elif action == "Slice":
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        left_part = raw_activation_key[:start_index]
        right_part = raw_activation_key[end_index:]
        raw_activation_key = left_part + right_part
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")













