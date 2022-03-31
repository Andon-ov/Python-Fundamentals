# number_of_lost_fight = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
# total_helmet_broke = number_of_lost_fight // 2
# total_sword_broke = number_of_lost_fight // 3
# total_shield_broke = number_of_lost_fight // 6
# total_armor_broke = total_shield_broke // 2
# total_money = (total_helmet_broke * helmet_price) + (total_sword_broke * sword_price) + \
#               (total_shield_broke * shield_price) + (total_armor_broke * armor_price)
# print(f'Gladiator expenses: {total_money:.2f} aureus')


lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_is_broken = lost_fights_count // 2
sword_is_broken = lost_fights_count // 3
shield_is_broken = lost_fights_count // 6
armor_is_broken = shield_is_broken // 2
total_price = (helmet_is_broken*helmet_price)+(sword_is_broken*sword_price)+\
              (shield_is_broken*shield_price)+(armor_is_broken*armor_price)

print(f"Gladiator expenses: {total_price:.2f} aureus")

