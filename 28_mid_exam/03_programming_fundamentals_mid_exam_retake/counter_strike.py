#
# initial_energy = int(input())
# distance_of_an_enemy = input()
# count = 0
#
# while not distance_of_an_enemy == "End of battle":
#
#     distance = int(distance_of_an_enemy)
#
#     if initial_energy < distance:
#         print(f"Not enough energy! Game ends with {count} won battles and {initial_energy} energy")
#         break
#     count += 1
#     initial_energy -= distance
#
#     if count % 3 == 0:
#         initial_energy += count
#     distance_of_an_enemy = input()
# if distance_of_an_enemy =="End of battle":
#     print(f'Won battles: {count}. Energy left: {initial_energy}')

initial_energy = int(input())
command = input()
won_battles = 0
while not command == "End of battle":
    enemy_health = int(command)
    if not enemy_health > initial_energy:
        initial_energy -= enemy_health
        won_battles += 1
        if won_battles % 3 == 0:
            initial_energy += won_battles
    else:
        print(f'Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy')
        exit()

    command = input()

print(f"Won battles: {won_battles}. Energy left: {initial_energy}")

















