# targets = [int(i) for i in input().split()]
# count = 0
# index = input()
#
# while not index == "End":
#     index = int(index)
#
#     if index not in range(len(targets)):
#         index = input()
#         continue
#
#     current_value = targets[index]
#
#     if current_value == -1:
#         index = input()
#         continue
#
#     targets[index] = -1
#     count += 1
#
#     for current_index in range(len(targets)):
#         if targets[current_index] == -1:
#             continue
#         if targets[current_index] > current_value:
#             targets[current_index] -= current_value
#         else:
#             targets[current_index] += current_value
#
#     index = input()
#
# print(f"Shot targets: {count} -> {' '.join([str(i) for i in targets])}")


targets = [int(x) for x in input().split()]
command = input()
while not command == "End":
    index = int(command)

    if 0 <= index < len(targets):

        for i in range(len(targets)):
            if index == i:
                continue
            if targets[index] >= targets[i]:
                if targets[i] > 0:
                    targets[i] += targets[index]
            elif targets[index] < targets[i]:
                if targets[i] > 0:
                    targets[i] -= targets[index]
        targets[index] = -1

    command = input()

print(f"Shot targets: {targets.count(-1)} -> {' '.join([str(x) for x in targets])}")











