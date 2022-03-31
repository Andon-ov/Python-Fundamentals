# free_chairs = 0
#
# are_chairs_enough = True
# n = int(input())
#
# for room_num in range(1, n+1):
#
#     chairs, people = input().split()
#     people = int(people)
#     difference = abs(len(chairs) - people)
#
#     if int(len(chairs))< people:
#
#         print(f'{difference} more chairs needed in room {room_num}')
#         are_chairs_enough = False
#     else:
#
#         free_chairs += difference
#
# if are_chairs_enough:
#     print(f'Game On, {free_chairs} free chairs left')

n = int(input())
free_chairs = 0
are_chairs_enough = True
for i in range(1, n + 1):

    command = input()
    split_command = command.split()
    chairs = split_command[0]
    people = int(split_command[1])

    difference = abs(len(chairs) - people)

    if len(chairs) < people:
        print(f"{difference} more chairs needed in room {i}")
        are_chairs_enough = False

    free_chairs += difference

if are_chairs_enough:
    print(f'Game On, {free_chairs} free chairs left')

















