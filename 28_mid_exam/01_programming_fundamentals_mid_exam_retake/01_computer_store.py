#
# sums = 0
# command = input()
# while not command in 'special' 'regular':
#
#     command = float(command)
#     if command < 0:
#         print('Invalid price!')
#         command = 0
#     else:
#         sums += command
#
#     command = input()
#
# taxes = sums * 0.20
# if sums == 0:
#     print('Invalid order!')
#     exit()
#
# if command == 'special':
#     total_price = (sums + taxes) * 0.9
# else:
#     total_price = (sums + taxes)
# print("Congratulations you've just bought a new computer!")
# print(f'Price without taxes: {sums:.2f}$')
# print(f'Taxes: {taxes:.2f}$')
# print(f'-----------')
# print(f'Total price: {total_price:.2f}$')



import sys
from io import StringIO

input1 = """1023 
15
-20
-5.50
450
20 
17.66 
19.30
regular"""

sys.stdin = StringIO(input1)
command = input()
total_price = 0
while True:
    if command == 'special' or command == 'regular':
        break

    if float(command) < 0:
        print('Invalid price!')
        command = input()
        continue

    else:
        total_price += float(command)

    command = input()
if total_price == 0:
    print("Invalid order!" )
else:
    taxes = total_price * 0.2
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    if command == 'special':
        print(f'Total price: {((total_price+taxes)*0.9):.2f}$')
    elif command == 'regular':
        print(f'Total price: {total_price+taxes:.2f}$')
