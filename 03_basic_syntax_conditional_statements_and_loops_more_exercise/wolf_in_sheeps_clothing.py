# sheep_or_wolf = input().split(", ")
#
# max_index = len(sheep_or_wolf)
# index_wolf = 0
#
# for index, wolf in enumerate(sheep_or_wolf):
#
#     if wolf == "wolf":
#         index_wolf = index
#     if wolf == "wolf" and (index == max_index - 1):
#         print("Please go away and stop eating my sheep")
#     elif wolf == "wolf" and (index < (len(sheep_or_wolf) - 1)):
#         print(f'Oi! Sheep number {(max_index - index_wolf)-1}! You are about to be eaten by a wolf!')



sheep_or_wolf = input().split(", ")
my_position = int(len(sheep_or_wolf)) -1
wolf_position = 0
for i in range(len(sheep_or_wolf)):
    if sheep_or_wolf[i] == 'wolf':
        wolf_position = i
if my_position == wolf_position:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {(len(sheep_or_wolf)-1) - wolf_position}! You are about to be eaten by a wolf!")


