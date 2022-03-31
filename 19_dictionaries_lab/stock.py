# data = input().split()
# searched_products = input().split()
# products = {}
# for i in range(0, len(data), 2):
#     key = data[i]
#     value = int(data[i + 1])
#     products[key] = value
#
# for s_p in searched_products:
#     if s_p in products:
#
#         print(f'We have {products[s_p]} of {s_p} left')
#     else:
#         print(f"Sorry, we don't have {s_p}")

products = input().split()


bakery = {}
for i in range(0,len(products),2):
    key = products[i]
    value = products[i+1]
    bakery[key] = value

# for i in range(len(searched_items)):
#
#     if searched_items[i] in bakery:
#         print(f"We have {bakery.get(searched_items[i])} of {searched_items[i]} left")
#     else:
#         print(f"Sorry, we don't have {searched_items[i]}")
searched_items = input().split()
for i in searched_items:

    if i in bakery:
        print(f"We have {bakery[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
