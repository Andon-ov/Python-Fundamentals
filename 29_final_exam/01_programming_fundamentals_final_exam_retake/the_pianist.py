# import sys
# from io import StringIO
#
# input1 = """3
# Fur Elise|Beethoven|A Minor
# Moonlight Sonata|Beethoven|C# Minor
# Clair de Lune|Debussy|C# Minor
# Add|Sonata No.2|Chopin|B Minor
# Add|Hungarian Rhapsody No.2|Liszt|C# Minor
# Add|Fur Elise|Beethoven|C# Minor
# Remove|Clair de Lune
# ChangeKey|Moonlight Sonata|C# Major
# Stop
# """
#
# sys.stdin = StringIO(input1)
#
# favorite_piano_pieces = {}
# n = int(input())
# for _ in range(n):
#     piece, composer, key = input().split("|")
#     if piece not in favorite_piano_pieces:
#         favorite_piano_pieces[piece] = [composer, key]
#
# command = input()
# while not command == "Stop":
#     split_command = command.split("|")
#     action = split_command[0]
#     piece = split_command[1]
#
#     if action == "Add":
#         composer = split_command[2]
#         key = split_command[3]
#         if piece in favorite_piano_pieces:
#             print(f"{piece} is already in the collection!")
#
#         elif piece not in favorite_piano_pieces:
#             favorite_piano_pieces[piece] = [composer, key]
#             print(f"{piece} by {composer} in {key} added to the collection!")
#
#     if action == "Remove":
#         if piece in favorite_piano_pieces:
#             print(f"Successfully removed {piece}!")
#             favorite_piano_pieces.pop(piece)
#
#         else:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#
#     if action == "ChangeKey":
#         new_key = split_command[2]
#         if piece in favorite_piano_pieces:
#             print(f"Changed the key of {piece} to {new_key}!")
#             favorite_piano_pieces[piece][1] = new_key
#         else:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#
#     command = input()
# favorite_piano_pieces = sorted(favorite_piano_pieces.items(), key=lambda kv: (kv[0], kv[1]))
# # Сортираме листа аз първо по key после по value!!!
#
# for key in favorite_piano_pieces:
#     print(f"{key[0]} -> Composer: {key[1][0]}, Key: {key[1][1]}")


import sys
from io import StringIO

input1 = """3
Fur Elise|Beethoven|A Minor
Moonlight Sonata|Beethoven|C# Minor
Clair de Lune|Debussy|C# Minor
Add|Sonata No.2|Chopin|B Minor
Add|Hungarian Rhapsody No.2|Liszt|C# Minor
Add|Fur Elise|Beethoven|C# Minor
Remove|Clair de Lune
ChangeKey|Moonlight Sonata|C# Major
Stop"""

input2 ="""4
Eine kleine Nachtmusik|Mozart|G Major
La Campanella|Liszt|G# Minor
The Marriage of Figaro|Mozart|G Major
Hungarian Dance No.5|Brahms|G Minor
Add|Spring|Vivaldi|E Major
Remove|The Marriage of Figaro
Remove|Turkish March
ChangeKey|Spring|C Major
Add|Nocturne|Chopin|C# Minor
Stop"""

sys.stdin = StringIO(input2)


def piece_in_collection(piece_name, piece_dict):
    if piece_name in piece_dict:
        return True


favorite_piano_pieces = {}
n = int(input())
for i in range(n):
    piece, composer, key = input().split("|")
    favorite_piano_pieces[piece] = [composer, key]

command = input()
while not command == "Stop":
    command_split = command.split("|")
    action = command_split[0]
    piece = command_split[1]

    if action == "Add":
        composer = command_split[2]
        key = command_split[3]
        if piece_in_collection(piece, favorite_piano_pieces):
            print(f"{piece} is already in the collection!")
        else:
            favorite_piano_pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        if not piece_in_collection(piece, favorite_piano_pieces):
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del favorite_piano_pieces[piece]
            print(f"Successfully removed {piece}!")

    elif action == "ChangeKey":
        new_key = command_split[2]
        if not piece_in_collection(piece, favorite_piano_pieces):
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            favorite_piano_pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

    command = input()
for key,value in favorite_piano_pieces.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")