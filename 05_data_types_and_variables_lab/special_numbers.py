#  със стринг
# end = int(input())
# for i in range(1, end + 1):
#     sum_of_digits = 0
#     digits = str(i)
#     for index, value in enumerate(digits):
#         sum_of_digits += int(value)
#     if sum_of_digits in (5, 7, 11):
#         print(f'{i} -> True')
#     else:
#         print(f'{i} -> False')

#  с делене
# end = int(input())
# for num in range(1, end +1):
#     temp_num = num
#     sum = 0
#     while temp_num > 0:
#         digit = temp_num % 10
#         sum += digit
#         temp_num = temp_num // 10
#     if sum in (5, 7, 11):
#         print(f'{num} -> True')
#     else:
#         print(f'{num} -> False')



# n = int(input())
#
# for num in range(1, n + 1):
#     num_as_string = str(num)
#     sum = 0
#
#     for symbol in num_as_string:
#         sum += int(symbol)
#
#     if sum in (5, 7, 11):
#         print(f'{num} -> True')
#
#     else:
#         print(f'{num} -> False')



# с Булен
# n = int(input())
# for num in range(1, n +1):
#     temp_num = num
#     sum = 0
#     while temp_num > 0:
#         digit = temp_num % 10
#         sum += digit
#         temp_num = temp_num // 10
#     is_special_number = sum in (5, 7, 11)
#     print(f'{num} -> {is_special_number}')


n = int(input())
for num in range(1, n +1):
    sum = 0

    while num:
        digit = num % 10
        sum += digit
        num = num // 10
    print(sum)


n = int(input())
for num in range(1, n + 1):
    num_as_string = str(num)
    sum = 0

    for symbol in num_as_string:
        sum += int(symbol)
    print(sum)

