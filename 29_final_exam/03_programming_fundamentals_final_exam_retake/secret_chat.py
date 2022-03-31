# import sys
# from io import StringIO
#
# input1 = """Hiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal
# """
#
# sys.stdin = StringIO(input1)
#
# concealed_message = input()
# command = input()
# while not command == "Reveal":
#     command_split = command.split(":|:")
#     action = command_split[0]
#
#     if action == "InsertSpace":
#         value = ' '
#         index = int(command_split[1])
#         left_part = concealed_message[:index]
#         right_part = concealed_message[index:]
#         concealed_message = left_part + value + right_part
#         print(concealed_message)
#
#     elif action == "Reverse":
#         substring = command_split[1]
#
#         if substring in concealed_message:
#             start_index = concealed_message.index(substring)
#             end_index = start_index + len(substring)
#             left_concealed_message = concealed_message[:start_index]
#             right_concealed_message = concealed_message[end_index:]
#
#             replacement = concealed_message[start_index:end_index]
#             concealed_message = left_concealed_message + right_concealed_message + replacement[::-1]
#             print(concealed_message)
#
#         else:
#             print("error")
#
#     elif action == "ChangeAll":
#         substring = command_split[1]
#         replacement = command_split[2]
#         concealed_message = concealed_message.replace(substring, replacement)
#         print(concealed_message)
#
#     command = input()
#
# print(f"You have a new text message: {concealed_message}")


import sys
from io import StringIO

input1 = """heVVodar!gniV
ChangeAll:|:V:|:l
Reverse:|:!gnil
InsertSpace:|:5
Reveal"""
input2 = """Hiware?uiy
ChangeAll:|:i:|:o
Reverse:|:?uoy
Reverse:|:jd
InsertSpace:|:3
InsertSpace:|:7
Reveal"""

sys.stdin = StringIO(input2)

message = input()
command = input()
while not command == "Reveal":
    command_split = command.split(":|:")
    action = command_split[0]
    if action == "InsertSpace":

        index = int(command_split[1])
        left_part = message[:index]
        right_part = message[index:]
        message = left_part + " " + right_part

        print(message)

    elif action == "Reverse":
        substring = command_split[1]

        if substring in message:

            index = message.index(substring)
            end = index + len(substring)
            left_part = message[:index]
            right_part = message[end:]
            replacement = message[index:end]
            message = left_part + right_part + replacement[::-1]
            print(message)

        else:
            print("error")

    elif action == "ChangeAll":
        substring = command_split[1]
        replacement = command_split[2]
        message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")
