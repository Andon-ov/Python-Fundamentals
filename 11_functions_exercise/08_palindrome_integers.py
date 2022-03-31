# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.
#
# def found_palindrome(num):
#     true_or_false = []
#     for i in num:
#         if i == i[:: - 1]:
#             true_or_false.append("True")
#
#         elif not i == i[:: - 1]:
#             true_or_false.append("False")
#
#     return true_or_false
#
#
# number = [i for i in input().split(', ')]
# result = found_palindrome(number)
# print('\n'.join(result))

def palindrome(nums):
    palindromes = []
    for i in number:
        if i[::-1] == i[::]:
            palindromes.append('True')
        else:
            palindromes.append('False')
    return palindromes


number = [i for i in input().split(', ')]
for i in palindrome(number):
    print(i)