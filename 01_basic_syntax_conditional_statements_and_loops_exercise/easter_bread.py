# budget = float(input())
# kg_flour = float(input())
# lose_eggs = 0
# eggs_pack_price = kg_flour * 0.75
# milk = (kg_flour * 1.25) / 4
# easter_bread = kg_flour + eggs_pack_price + milk
# how_many_easter_bread = int(budget // easter_bread)
# colored_eggs = (how_many_easter_bread * 3)
# money_left = budget - (how_many_easter_bread * easter_bread)
# for i in range(1, how_many_easter_bread + 1):
#     if i % 3 == 0:
#         lose_eggs += (i - 2)
#
# print(f"You made {how_many_easter_bread:.0f} loaves of Easter bread! Now you have "
#       f"{(colored_eggs - lose_eggs):.0f} eggs and {money_left:.2f}BGN left.")



budget = float(input())
kg_flour = float(input())
lose_eggs = 0
eggs_pack_price = kg_flour * 0.75
milk = (kg_flour * 1.25) / 4
easter_bread = kg_flour + eggs_pack_price + milk
how_many_easter_bread = int(budget/easter_bread)
colored_eggs = (how_many_easter_bread * 3)
budget_left = budget-(how_many_easter_bread*easter_bread)
for i in range(1,how_many_easter_bread +1):
    if i % 3 == 0:
        colored_eggs -= (i - 2)
print(f"You made {how_many_easter_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget_left:.2f}BGN left.")