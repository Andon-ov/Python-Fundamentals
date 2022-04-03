import sys
from io import StringIO

input1 = """ILikeSoftUni
Replace I We
Make Upper
Check SoftUni
Sum 1 4
Cut 1 4
Finish"""
input2 = """HappyNameDay
Replace p r
Make Lower
Cut 2 23
Sum -2 2
Finish"""
input3 = """"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

def valid_index(string, index):
    if 0 <= index < len(string):
        return True
    return False


text = input()
command = input()
while not command == "Finish":
    command_split = command.split()
    action = command_split[0]

    if action == "Replace":

        my_char = command_split[1]
        new_char = command_split[2]
        text = text.replace(my_char, new_char)
        print(text)

    elif action == "Cut":
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        if valid_index(text, start_index) and valid_index(text, end_index):
            left_part = text[:start_index]
            right_part = text[end_index + 1:]
            text = left_part + right_part
            print(text)
        else:
            print("Invalid indices!")

    elif action == "Make":
        upper_lower = command_split[1]
        if upper_lower == "Upper":
            text = text.upper()
            print(text)
        else:
            text = text.lower()
            print(text)

    elif action == "Check":
        string = command_split[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif action == "Sum":
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        if valid_index(text, start_index) and valid_index(text, end_index):
            new_text = text[start_index:end_index + 1]
            char_sum = 0
            for i in new_text:
                char_sum += ord(i)
            print(char_sum)
        else:
            print("Invalid indices!")

    command = input()
