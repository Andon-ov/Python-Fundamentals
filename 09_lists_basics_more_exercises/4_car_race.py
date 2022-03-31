# left_sum = 0
# right_sum = 0
#
# track = [int(i) for i in input().split()]
# middle = len(track)//2
#
# left_side = track[:middle]
# reflect_side = track[::-1]
# right_side = reflect_side[:middle]
#
# for numbers in left_side:
#     if numbers == 0:
#         left_sum *= 0.8
#     left_sum += numbers
#
# for numbers in right_side:
#     if numbers == 0:
#         right_sum *= 0.8
#     right_sum += numbers
#
# if left_sum < right_sum:
#     print(f"The winner is left with total time: {left_sum:.1f}")
# elif left_sum > right_sum:
#     print(f"The winner is right with total time: {right_sum:.1f}")


def first(track, end):
    time = 0
    first_car = track[: end]
    for i in first_car:
        if i == 0:
            time *= 0.8
        time += i
    return time


def second(track, end):
    time = 0
    second_car = track[end + 1::]
    second_car = second_car[::-1]
    for i in second_car:
        if i == 0:
            time *= 0.8
        time += i
    return time


race = [int(i) for i in input().split()]
finish = len(race) // 2
left_car = first(race, finish)
right_car = second(race, finish)
if left_car < right_car:
    print(f'The winner is left with total time: {left_car:.1f}')
else:
    print(f'The winner is right with total time: {right_car:.1f}')
