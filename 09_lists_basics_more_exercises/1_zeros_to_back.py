# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements.
# Print the resulting integer list.


# ready_nums = []
# count = 0
#
# numbers = input()
# nums = (numbers.split(", "))
#
# for string in nums:
#
#     if string == "0":
#         count += 1
#
#     else:
#         ready_nums.append(string)
#
# for j in range(count):
#
#     ready_nums.append('0')
#
# for index in range(len(ready_nums)): # от лист със стринг на лист с инт
#     ready_nums[index] = int(ready_nums[index])
#
# print(ready_nums)

numbers = [int(i) for i in input().split(", ")]
zero = numbers.count(0)
for i in range(zero):
    numbers.remove(0)
    numbers.append(0)
print(numbers)
