# order = {}
# command = input()
# while not command == 'buy':
#     command_split = command.split( )
#
#     name = command_split[0]
#     price = float(command_split[1])
#     quantity = float(command_split[2])

#     if name not in order:
#         order[name] = []
#         order[name].append(price)
#         order[name].append(quantity)
#     else:
#         order[name][1] += quantity
#         order[name][0] = price
#
#     command = input()
#
# for key , value in order.items():
#     print(f"{key} -> {(value[0]*value[1]):.2f}")

orders = {}
command = input()
while not command == 'buy':
    command_split = command.split()
    product = command_split[0]
    price = float(command_split[1])
    quantity = int(command_split[2])

    if product not in orders:
        orders[product] = []
        orders[product].append(price)
        orders[product].append(quantity)
    else:
        orders[product][0] = price
        orders[product][1] += quantity

    command = input()
for key, value in orders.items():
    print(f"{key} -> {(value[0] * value[1]):.2f}")
