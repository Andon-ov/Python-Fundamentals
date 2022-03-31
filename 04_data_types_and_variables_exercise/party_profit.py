# import math
# companions = int(input())
# days = int(input())
# total_coins = 0
# for day in range(1, days + 1):
#     if day % 10 == 0:
#         companions -= 2
#     if day % 15 == 0:
#         companions += 5
#     if day % 3 == 0:
#         total_coins -= companions * 3
#     if day % 5 == 0:
#         total_coins += companions * 20
#         if day % 3 == 0:
#             total_coins -= companions * 2
#     total_coins += 50
#     total_coins -= companions * 2
# coins_per_companion = total_coins // companions
# print(f'{companions} companions received {coins_per_companion} coins each.')


group_size = int(input())
n = int(input())
coins = 0
for i in range(1,n+1):

    # Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave,
    if i % 10 == 0:
        group_size -= 2

    # but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
    if i % 15 == 0:
        group_size += 5

    # Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
    coins += 50
    coins -= 2 * group_size

    # Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
    if i % 3 == 0:
        coins -= 3 * group_size

    # Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion.
    if i % 5 == 0:
        coins += 20 * group_size

        # But if you have a motivational party the same day, you spend additional 2 coins per companion.
        if i % 3 == 0:
            coins -= 2 * group_size

# You should calculate how many coins gets each companion at the end of the adventure.
print(f"{group_size} companions received {int(coins/group_size)} coins each.")
# Note: You cannot split a coin, so you should round down the coins to an integer number.









