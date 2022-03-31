# items = input().split('|')
# budget = int(input())
# my_items = []
#
# for index in range(len(items)):
#     item, price = items[index].split('->')
#     if item == 'Clothes':
#         if float(price) <= 50:
#             if budget >= float(price):
#                 my_items.append(price)
#                 budget -= float(price)
#
#         continue
#
#     elif item == 'Shoes':
#         if float(price) <= 35:
#             if budget >= float(price):
#                 my_items.append(price)
#                 budget -= float(price)
#         continue
#
#     elif item == 'Accessories':
#         if float(price) <= 20.50:
#             if budget >= float(price):
#                 my_items.append(price)
#                 budget -= float(price)
#         continue
# total_sum = [float(i) * 1.40 for i in my_items]
# hello_france = sum(total_sum) + budget
# sums = [float(i) * 0.40 for i in my_items]
# final_sum = sum(sums)
# if hello_france >= 150:
#
#     for i in range(len(total_sum)):
#         print(f'{total_sum[i]:.2f}',end=' ')
#     print()
#     print(f'Profit: {final_sum:.2f}')
#     print('Hello, France!')
# else:
#     for i in range(len(total_sum)):
#         print(f'{total_sum[i]:.2f}', end=' ')
#     print()
#     print(f'Profit: {final_sum:.2f}')
#     print('Not enough money.')







# train ticket to France costs exactly 150$
# higher price – with a 40% markup
# Clothes	    50.00
# Shoes	        35.00
# Accessories	20.50


items = input().split('|')
budget = int(input())
profit = 0
items_for_sell = [] # predi da gi dobawq da im slova 40% nadcenka
for i in items:
    command = i.split('->')
    item = command[0]
    price = float(command[1])

    if item == 'Clothes':
        if 0 <= price <= 50:
            if budget >= price:
                budget -= price
                items_for_sell.append(price*1.4)
                profit += price * 0.4
    elif item == 'Shoes':
        if 0 <= price <= 35:
            if budget >= price:
                budget -= price
                items_for_sell.append(price*1.4)
                profit += price * 0.4
    elif item == 'Accessories':
        if 0 <= price <= 20.50:
            if budget >= price:
                budget -= price
                items_for_sell.append(price*1.4)
                profit += price * 0.4
for i in items_for_sell:
    print(f'{i:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if sum(items_for_sell) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
