
# import sys
#
# numbers = [int(i) for i in input().split()]
# n = int(input())
#
# for i in range(n):
#     min_num = sys.maxsize
#
#     for nums in numbers:
#         if nums < min_num:
#             min_num = nums
#
#     numbers.remove(min_num)
# print(', '.join([str(i) for i in numbers]))


numbers = [int(i) for i in input().split()]
n = int(input())

for i in range(n):
    min_num = min(numbers)
    numbers.remove(min_num)
print(', '.join([str(i) for i in numbers]))
