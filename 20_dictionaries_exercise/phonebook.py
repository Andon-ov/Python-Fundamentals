# contacts = {}
#
# data = input()
# while "-" in data:
#
#     name, number = data.split("-")
#     contacts[name] = number
#
#     data = input()
# if data.isdigit():
#     n = int(data)
#
# for i in range(n):
#     names = input()
#     for key, value in contacts.items():
#         if names in key:
#             print(f"{key} -> {value}")
#     if names not in contacts.keys():
#         print(f"Contact {names} does not exist.")


phonebook = {}
command = input()
while not command.isnumeric():

    command_split = command.split('-')
    name = command_split[0]
    phone = command_split[1]

    if name not in phonebook:
        phonebook[name] = phone
    command = input()

n = int(command)

for _ in range(n):
    name = input()

    if name in phonebook:
        for key, value in phonebook.items():
            if name == key:
                print(f"{key} -> {value}")
    else:
        print(f"Contact {name} does not exist.")
