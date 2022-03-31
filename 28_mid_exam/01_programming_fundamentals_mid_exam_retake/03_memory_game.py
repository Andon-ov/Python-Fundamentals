# count = 0
# memory_game = input().split()
# command = input()
#
# while not command == "end":
#     command_args = command.split()
#     first_index = int(command_args[0])
#     second_index = int(command_args[1])
#     count += 1
#     if first_index == second_index or first_index < 0 or second_index < 0 or first_index >= len(
#             memory_game) or second_index >= len(memory_game):
#
#         middle = len(memory_game)//2
#         new_item = f'-{count}a'
#         memory_game.insert(middle,new_item)
#         memory_game.insert(middle,new_item)
#         print(f'Invalid input! Adding additional elements to the board')
#
#     elif memory_game[first_index] == memory_game[second_index]:
#         remove_item = memory_game.pop(first_index)
#         memory_game.remove(remove_item)
#         print(f'Congrats! You have found matching elements - {remove_item}!')
#
#         if len(memory_game) ==0:
#             break
#
#     elif memory_game[first_index] != memory_game[second_index]:
#         print('Try again!')
#
#     command = input()
#
# if len(memory_game) > 0:
#     print('Sorry you lose :(')
# elif len(memory_game) == 0:
#     print(f'You have won in {count} turns!')
# print(' '.join(memory_game))


import sys
from io import StringIO

input1 = """a 2 4 a 2 4
0 3
0 2
0 1
0 1
end"""

sys.stdin = StringIO(input1)
game = input().split()
numbers = input()
count = 0
while not numbers == "end":
    split_numbers = numbers.split()
    count += 1
    index_one = int(split_numbers[0])
    index_two = int(split_numbers[1])
    if index_one == index_two or (not 0 <= index_one < len(game)) or (not 0 <= index_two < len(game)):
        print('Invalid input! Adding additional elements to the board')
        add = f"-{count}a"
        center = int(len(game) / 2)

        game.insert(center, add)
        game.insert(center, add)

    elif game[index_one] == game[index_two]:
        print(f'Congrats! You have found matching elements - {game[index_one]}!')
        one = game[index_one]
        two = game[index_two]
        game.remove(one)
        game.remove(two)
        if len(game) == 0:
            break
    elif not game[index_one] == game[index_two]:
        print("Try again!")

    numbers = input()

if len(game) > 0:
    print(f'Sorry you lose :(')
    print(' '.join([str(x) for x in game]))
else:
    print(f'You have won in {count} turns!')
