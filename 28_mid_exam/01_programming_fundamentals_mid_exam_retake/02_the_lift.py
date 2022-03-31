# people = int(input())
# wagon = [int(i) for i in list(input().split())]
#
# free_space = (len(wagon)*4) - sum(wagon)
#
# if free_space > people:
#     print('The lift has empty spots!')
#
#     for index, value in enumerate(wagon):
#         free_place = 4 - value
#         if value < 4 and (people > free_place and not people ==0):
#
#             wagon[index] += free_place
#             people -= free_place
#
#         elif people <= 4 and free_place <= 4 and free_place !=0 :
#             last_people = people
#             wagon[index] += last_people
#             people -= last_people
#
#             if people == 0:
#                 break
#
# elif free_space < people:
#     print(f"There isn't enough space! {abs(free_space - people)} people in a queue!")
#     for i in range(len(wagon)):
#         wagon[i] = 4
#
# elif free_space == people:
#
#     for i in range(len(wagon)):
#         wagon[i] = 4
# print(" ".join([str(i) for i in wagon]))
#

# import sys
# from io import StringIO
#
# input1 = """20
# 0 2 0"""
#
# sys.stdin = StringIO(input1)

how_many_people_waiting = int(input())
lift = [int(x) for x in input().split()]
for i in range(len(lift)):

    if lift[i] < 4:
        add = 4 - lift[i]
        if add > how_many_people_waiting:
            lift[i] += how_many_people_waiting
            how_many_people_waiting -= lift[i]
            break
        lift[i] += add
        how_many_people_waiting -= add

if sum(lift) == len(lift) * 4:
    print(f"There isn't enough space! {how_many_people_waiting} people in a queue!")
    print(' '.join([str(x) for x in lift]))
else:
    print(f'The lift has empty spots!')
    print(' '.join([str(x) for x in lift]))
# ToDO 90/`100












