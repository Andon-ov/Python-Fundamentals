# version_string_as_list = input().split('.')
# int_number = int(''.join(version_string_as_list) ) + 1
# new_version = list(str(int_number))
# print('.'.join(new_version))


# version = [int(i) for i in input().split('.')]
# version[-1] += 1
# for current_index in range(len(version) - 1, - 1, - 1):
#     if version[current_index] > 9:
#         version[current_index] = 0
#         if current_index - 1 >= 0:
#             version[current_index - 1] += 1
# print('.'.join([str(s) for s in version]))


print('.'.join([str(x) for x in list(str(int(''.join([str(x) for x in input().split('.')])) + 1))]))


# version = int(''.join([str(x) for x in input().split('.')])) + 1
# new_version = list(str(version))
# print('.'.join([str(x) for x in new_version]))
















