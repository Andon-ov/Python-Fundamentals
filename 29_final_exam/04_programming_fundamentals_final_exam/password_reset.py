# password = input()
# command = input()
# while not command == "Done":
#     command_split = command.split()
#     action = command_split[0]
#     if action == "TakeOdd":
#         new_password = ''
#         for i in range(len(password)):
#             if not i % 2 == 0:
#                 new_password += password[i]
#         password = new_password
#         print(password)
#
#     elif action == "Cut":
#         start_index = int(command_split[1])
#         end_index = start_index + int(command_split[2])
#         left_part = password[:start_index]
#         right_part = password[end_index:]
#         password = left_part + right_part
#         print(password)
#     elif action == "Substitute":
#         old_string = command_split[1]
#         new_string = command_split[2]
#
#         if old_string not in password:
#             print("Nothing to replace!")
#         else:
#             password = password.replace(old_string,new_string)
#             print(password)
#
#     command = input()
#
# print(f"Your password is: {password}")

import sys
from io import StringIO

input1 = """Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr 
TakeOdd
Cut 15 3
Substitute :: -
Substitute | ^
Done"""
input2 = """up8rgoyg3r1atmlmpiunagt!-irs7!1fgulnnnqy
TakeOdd
Cut 18 2
Substitute ! ***
Substitute ? .!.
Done"""


sys.stdin = StringIO(input2)


password = input()
command = input()
while not command == "Done":
    command_split = command.split()
    action = command_split[0]

    if action == "TakeOdd":
        new_pass = ""
        for i in range(len(password)):
            if i % 2 != 0:
                new_pass += password[i]
        password = new_pass
        print(password)

    elif action == "Cut":
        index = int(command_split[1])
        length = int(command_split[2])
        left_part = password[:index]
        middle_part = password[index:index+length]
        right_part = password[index+length:]
        password = left_part +  right_part
        print(password)

    elif action == "Substitute":

        substring = command_split[1]
        substitute = command_split[2]
        if substring in password:
            password = password.replace(substring,substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")























