# my_health = 100
# bitcoins = 0
# i_im_death = False
# best_room = 0
# string = input().split('|')
# for i in string:
#     best_room += 1
#     action, amount = i.split(' ')
#
#     if action == "potion":
#         if my_health > 100:
#             my_health = 100
#
#         elif my_health + int(amount) < 100:
#             my_health += int(amount)
#             print(f'You healed for {amount} hp.')
#             print(f"Current health: {my_health} hp.")
#
#         elif my_health + int(amount) > 100:
#             print(f'You healed for {abs(my_health - 100)} hp.')
#             my_health += int(amount)
#             my_health = 100
#             print(f"Current health: {my_health} hp.")
#
#     elif action == "chest":
#         bitcoins += int(amount)
#         print(f"You found {amount} bitcoins.")
#
#     else:
#         if my_health > 0:
#             if my_health > int(amount):
#                 my_health -= int(amount)
#                 print(f"You slayed {action}.")
#             elif my_health <= int(amount):
#                 i_im_death = True
#                 print(f"You died! Killed by {action}.")
#                 break
#
# if i_im_death:
#     print(f'Best room: {best_room}')
# else:
#     print(f"You've made it!")
#     print(f"Bitcoins: {bitcoins}")
#     print(f"Health: {my_health}")

health = 100
bitcoins = 0
best_room = 0
i_im_death = False
dungeons_rooms = input().split('|')
for i in range(len(dungeons_rooms)):
    split = dungeons_rooms[i].split()
    string = split[0]
    number = int(split[1])
    best_room += 1

    if string == 'potion':
        if number + health < 100:
            health += number
            print(f'You healed for {number} hp.')
            print(f"Current health: {health} hp.")
        elif number + health > 100:
            print(f'You healed for {abs(health - 100)} hp.')
            health = 100
            print(f"Current health: {health} hp.")

    elif string == 'chest':
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        if number >= health:
            print(f"You died! Killed by {string}.")
            i_im_death = True
            break

        elif number < health:
            health -= number
            print(f'You slayed {string}.')

if i_im_death:
    print(f'Best room: {best_room}')
else:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")



















