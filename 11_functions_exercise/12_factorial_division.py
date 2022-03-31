# import math
#
# number_one = int(input())
# number_two = int(input())
#
# result = math.factorial(number_one) / math.factorial(number_two)
# print(f'{result:.2f}')



def factorial(num):
    sum = 1
    for i in range(1, num + 1):
        sum *= i
    return sum


number_one, number_two = int(input()), int(input())
print(f'{factorial(number_one)/factorial(number_two):.2f}')




# def factorial_division(first_number, second_number):
#
#     for i in range(first_number - 1, 0, -1):
#         first_number *= i
#
#     for i in range(second_number - 1, 0, -1):
#         second_number *= i
#
#     final_number = first_number / second_number
#
#     return f'{final_number:.2f}'
#
#
# number_one = int(input())
# number_two = int(input())
#
# print(factorial_division(number_one,number_two))


# first_number = int(input())
# second_number = int(input())
#
#
# for i in range(first_number -1,0,-1):
#     first_number *= i
#
# for i in range(second_number -1,0,-1):
#     second_number *= i
#
#
# final_number = first_number / second_number
#
# print(f'{final_number:.2f}')




