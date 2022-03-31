# def multiplied_character_codes(shor_string,long_string):
#     total_sum = 0
#     differance = abs(len(shor_string) - len(long_string))
#
#     for index in range(0, len(shor_string)):
#         total_sum += ord(long_string[index]) * ord(shor_string[index])
#
#     for index in range(len(long_string) - differance, len(long_string)):
#         total_sum += ord(long_string[index])
#     return total_sum
#
#
# first_string, second_string = input().split()
# string = 0
#
# if len(first_string) > len(second_string):
#     string = multiplied_character_codes(second_string,first_string)
#
# elif len(second_string) > len(first_string):
#     string = multiplied_character_codes(first_string, second_string)
#
# else:
#     string = multiplied_character_codes(first_string, second_string)
# print(string)


one = []
two = []

string = input().split()

for i in range(len(string[0])):
    one.append(ord(string[0][i]))

for i in range(len(string[1])):
    two.append(ord(string[1][i]))

sum = 0

if len(one) > len(two):
    point = len(two) - len(one)

    for i in range(len(two)):
        sum += one[i] * two[i]

    for i in range(-1, point - 1, -1):
        sum += one[i]

else:
    point = len(one) - len(two)

    for i in range(len(one)):
        sum += one[i] * two[i]

    for i in range(-1, point - 1, -1):
        sum += two[i]

print(sum)
