# import sys
# from io import StringIO
#
# input1 = """Albania:Bulgaria:Cyprus:Deuchland
# Add Stop:3:Nigeria
# Remove Stop:4:8
# Switch:Albania: Azərbaycan
# Travel
# """
#
# sys.stdin = StringIO(input1)
#
#
# def valid_index(string,index):
#     if 0 <= index <len(string):
#         return True
#     return False
#
#
# world_tour = input()
# command = input()
# while not command == "Travel":
#     command_split = command.split(":")
#     action = command_split[0]
#
#     if action == "Add Stop":
#         index = int(command_split[1])
#         string = command_split[2]
#         if valid_index(world_tour,index):
#             left_part = world_tour[:index]
#             right_part = world_tour[index:]
#             world_tour = left_part + string + right_part
#             print(world_tour)
#         else:
#             print(world_tour)
#
#
#     elif action == "Remove Stop":
#         start_index = int(command_split[1])
#         end_index = int(command_split[2])
#         if valid_index(world_tour,start_index) and valid_index(world_tour,end_index):
#             left_part = world_tour[:start_index]
#             right_part = world_tour[end_index+1:]
#             world_tour = left_part + right_part
#             print(world_tour)
#         else:
#             print(world_tour)
#
#     elif action == "Switch":
#         old_string = command_split[1]
#         new_string = command_split[2]
#         if old_string in world_tour:
#             world_tour = world_tour.replace(old_string,new_string)
#             print(world_tour)
#
#         else:
#             print(world_tour)
#
#     command = input()
# print(f"Ready for world tour! Planned stops: {world_tour}")

#
# import sys
# from io import StringIO
#
# input1 = """Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel"""
# input2 = """"""
#
# sys.stdin = StringIO(input1)
#
#
# def index_is_valid(text, index):
#     if 0 <= index < len(text):
#         return True
#
#
# text = input()
# command = input()
# while not command == "Travel":
#     command_split = command.split(":")
#     action = command_split[0]
#
#     if action == "Add Stop":
#         index = int(command_split[1])
#         string = command_split[2]
#         if index_is_valid(text, index):
#             left_part = text[:index]
#             right_part = text[index:]
#             text = left_part + string + right_part
#
#         print(text)
#
#     elif action == "Remove Stop":
#         start_index = int(command_split[1])
#         end_index = int(command_split[2])
#         if index_is_valid(text, start_index) and index_is_valid(text, end_index):
#             left_part = text[:start_index]
#             right_part = text[end_index + 1:]
#             text = left_part + right_part
#
#         print(text)
#
#     elif action == "Switch":
#         old_string = command_split[1]
#         new_string = command_split[2]
#         if old_string in text:
#             text = text.replace(old_string, new_string)
#
#         print(text)
#
#     command = input()
# print(f"Ready for world tour! Planned stops: {text}")


import sys
from io import StringIO

input1 = """Hawai::Cyprys-Greece
Add Stop:7:Rome
Remove Stop:11:16
Switch:Hawai:Bulgaria
Travel"""
input2 = """"""

sys.stdin = StringIO(input1)


def index_is_valid(index, string):
    if 0 <= index < len(string):
        return True
    return False


string = input()
command = input()

while not command == "Travel":
    command_split = command.split(":")
    action = command_split[0]
    if action == "Add Stop":

        index = int(command_split[1])
        new_string = command_split[2]
        left_part = string[:index]
        right_part = string[index:]

        if index_is_valid(index, string):
            string = left_part + new_string + right_part

        print(string)

    elif action == "Remove Stop":
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        left_part = string[:start_index]
        right_part = string[end_index+1:]
        if index_is_valid(start_index, string) and index_is_valid(end_index, string):
            string = left_part + right_part

        print(string)

    elif action == "Switch":
        old_string = command_split[1]
        new_string = command_split[2]
        string = string.replace(old_string, new_string)

        print(string)

    command = input()
print(f"Ready for world tour! Planned stops: {string}")
