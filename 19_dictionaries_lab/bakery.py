# products = input().split()
#
# bakery = {}
# for i in range(0, len(products), 2):
#     key = products[i]
#     value = int(products[i + 1])
#     bakery[key] = value
# print(bakery)
#
products = input().split()

bakery = {}
for i in range(0,len(products),2):
    key = products[i]
    value = products[i+1]
    bakery[key] = value

print(bakery)