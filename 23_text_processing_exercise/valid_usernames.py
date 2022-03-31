# def length(username):
#     if 3 <= len(username) <= 16:
#         return True
#     return False
#
#
# def type_of_symbols(username):
#     for character in username:
#         if not (character.isalnum() or character == '_' or character == '-'):
#             return False
#     return True
#
#
# def redundant(username):
#     for character in username:
#         if character == ' ':
#             return False
#     return True
#
#
# def username_is_valid(username):
#     if length(username) and type_of_symbols(username) and redundant(username):
#         return True
#
#
# usernames = input().split(', ')
# for username in usernames:
#     if username_is_valid(username):
#         print(username)
#


import sys
from io import StringIO

input1 = """Jeff, john45, ab, cd, peter-ivanov, @smith"""

sys.stdin = StringIO(input1)


def word_length(word):
    if 3 <= len(word) <= 16:
        return True
    return False


def word_contain(word):
    if word.isidentifier() or "-" in word:
        return True
    return False


def redundant_symbols(word):
    if " " not in word:
        return True
    return False


def all_is_true(word):
    if word_length(word) and word_contain(word) and redundant_symbols(word):
        return True


text = input().split(", ")
for word in text:
    if all_is_true(word):
        print(word)
