# data = input()
# products = {}
# while not data == 'statistics':
#     product_name,product_quantity = data.split(': ')
#     if product_name in products:
#         products[product_name] += int(product_quantity)
#     else:
#         products[product_name] = int(product_quantity)
#     data = input()
# print('Products in stock:')
# for key,value in products.items():
#     print(f'- {key}: {value}')
# print(f'Total Products: {len(products)}')
# print(f'Total Quantity: {sum(products.values())}')

command = input()
products = {}
while not command == "statistics":
    key, value = command.split(': ')
    if key not in products:
        products[key] = int(value)
    else:
        products[key] += int(value)

    command = input()
print('Products in stock:')
for key, value in products.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')


# command = input()
# products = {}
# while not command == "statistics":
#     key, value = command.split(': ')
#     #  опция и без if, else която е проверяваме дали Ключа го има в списъка и ако го няма го добавяме със стойност 0
#     if key not in products:
#         products[key] = 0
#     products[key] += int(value)
#
#     command = input()
# print('Products in stock:')
# for key, value in products.items():
#     print(f'- {key}: {value}')
# print(f'Total Products: {len(products)}')
# print(f'Total Quantity: {sum(products.values())}')