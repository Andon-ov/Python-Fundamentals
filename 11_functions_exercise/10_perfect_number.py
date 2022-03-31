def perfect_number(is_perfect_number):
    sums = 0
    for i in range(1,is_perfect_number):
        if is_perfect_number % i == 0:
            sums += i

    if sums == is_perfect_number:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."

number = int(input())
print(perfect_number(number))


# def perfect_number(num):
#     sum = 0
#     for i in range(num - 1, 0, -1):
#         if num % i == 0:
#             sum += i
#
#     if sum == num:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# number = int(input())
# print(perfect_number(number))


