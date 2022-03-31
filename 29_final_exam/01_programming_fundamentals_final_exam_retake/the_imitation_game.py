# def move(word,n):
#     new_word = word[n:]
#     first_char = word[:n]
#     last_word = new_word + first_char
#     return last_word
#
#
# def insert(word,n,char):
#     new_word_start = word[:n]
#     new_word_end = word[n:]
#     last_word = new_word_start + char + new_word_end
#     return last_word
#
#
# def change_all(word,char,new_char):
#     last_word = ''
#     for i in word:
#         if not i == char:
#             last_word += i
#         else:
#             last_word += new_char
#     return last_word
#
#
# string = input()
# command = input()
#
# while not command == "Decode":
#
#     split_command = command.split('|')
#     action = split_command[0]
#
#     if action == 'Move':
#         n = int(split_command[1])
#         last_word = move(string,n)
#         string = last_word
#
#     elif action == 'Insert':
#         n = int(split_command[1])
#         char = split_command[2]
#         last_word = insert(string,n,char)
#         string = last_word
#
#     elif action == 'ChangeAll':
#         char = split_command[1]
#         new_char = split_command[2]
#         last_word = change_all(string,char,new_char)
#         string = last_word
#
#     command = input()
#
# print(f"The decrypted message is: {string}")


# import sys
# from io import StringIO
#
# input1 = """zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode
# """
#
# sys.stdin = StringIO(input1)
#
# word = input()
# code = input()
# while not code == "Decode":
#
#     split_code = code.split("|")
#     action = split_code[0]
#     if action == 'Move':
#
#         index = int(split_code[1])
#         left_side = word[:index]
#         right_side = word[index:]
#         word = right_side + left_side
#
#     elif action == 'Insert':
#
#         index = int(split_code[1])
#         value = split_code[2]
#         left_side = word[:index]
#         right_side = word[index:]
#         word = left_side + value + right_side
#
#     elif action == 'ChangeAll':
#
#         old_letter = split_code[1]
#         new_letter = split_code[2]
#         word = word.replace(old_letter, new_letter)
#
#     code = input()
#
# print(f"The decrypted message is: {word}")


import sys
from io import StringIO

input1 = """zzHe
ChangeAll|z|l
Insert|2|o
Move|3
Decode"""

input2 = """owyouh
Move|2
Move|3
Insert|3|are
Insert|9|?
Decode"""

sys.stdin = StringIO(input2)

encrypted_message = input()
command = input()
while not command == "Decode":
    split_command = command.split('|')
    action = split_command[0]
    if action == "Move":

        number_of_letters = int(split_command[1])
        end = encrypted_message[:number_of_letters]
        start = encrypted_message[number_of_letters:]
        encrypted_message = start + end

    elif action == "Insert":
        index = int(split_command[1])
        value = split_command[2]
        start = encrypted_message[:index]
        end = encrypted_message[index:]
        encrypted_message = start + value + end

    elif action == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]
        encrypted_message = encrypted_message.replace(substring,replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")
