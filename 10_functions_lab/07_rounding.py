# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().
numbers = ([float(i) for i in input().split()])
rounded_numbers = []
for nums in numbers:
    round_nums = round(nums)
    rounded_numbers.append(round_nums)

print(rounded_numbers)