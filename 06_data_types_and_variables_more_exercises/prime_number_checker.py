# num = int(input())
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print('False')
#             break
#     else:
#         print('True')
#
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#     print('False')
#






# A prime number is a natural number greater than 1, not a product of two smaller natural numbers.
# For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.

number = int(input())
if number > 1: # Проверяваме дали числото е по голямо от едно!
    for i in range(2,number): # Въртим цикъл от 2 до числото (ако е прайм няма да се дели на нито едно число)
        if number % i == 0: # Ако с раздели на някое число значи не е праим - принтираме и прекъсваме цикала
            print('False')
            break
    else:
        print('True')

else:
    print('True')


































