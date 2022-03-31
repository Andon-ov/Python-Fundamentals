# import sys
# from io import StringIO
#
# input1 = """4
# Adela 90 150
# SirMullich 70 40
# Ivor 1 111
# Tyris 94 61
# Heal - SirMullich - 50
# Recharge - Adela - 100
# CastSpell - Tyris - 1000 - Fireball
# TakeDamage - Tyris - 99 - Fireball
# TakeDamage - Ivor - 3 - Mosquito
# End
#
# """
#
# sys.stdin = StringIO(input1)
#
#
# def hero_append(hcl: dict, text):
#     split_text = text.split()
#     hero = split_text[0]
#     hp = int(split_text[1])
#     mp = int(split_text[2])
#     hcl[hero] = [hp, mp]
#     return hcl
#
#
# # a hero can have a maximum of 100 HP and 200 MP
# hcl = {}
# n = int(input())
# for _ in range(n):
#     text = input()
#     hero_append(hcl, text)
#
# command = input()
# while not command == "End":
#
#     split_command = command.split(" - ")
#
#     action = split_command[0]
#     hero = split_command[1]
#
#     if action == "CastSpell":
#         mp_needed = int(split_command[2])
#         spell_name = split_command[3]
#         if hcl[hero][1] >= mp_needed:
#             hcl[hero][1] -= mp_needed
#             print(f"{hero} has successfully cast {spell_name} and now has {hcl[hero][1]} MP!")
#
#         else:
#             print(f"{hero} does not have enough MP to cast {spell_name}!")
#
#     elif action == "TakeDamage":
#         damage = int(split_command[2])
#         attacker = split_command[3]
#         hcl[hero][0] -= damage
#         if hcl[hero][0] > 0:
#             print(f"{hero} was hit for {damage} HP by {attacker} and now has {hcl[hero][0]} HP left!")
#         else:
#             print(f"{hero} has been killed by {attacker}!")
#             del hcl[hero]
#
#     elif action == "Recharge":
#         mp_amount = int(split_command[2])
#         if hcl[hero][1] + mp_amount <= 200:
#             hcl[hero][1] += mp_amount
#             print(f"{hero} recharged for {mp_amount} MP!")
#         else:
#             print(f"{hero} recharged for {200 - hcl[hero][1]} MP!")
#             hcl[hero][1] = 200
#
#     elif action == "Heal":
#         hp_amount = int(split_command[2])
#
#         if hcl[hero][0] + hp_amount <= 100:
#             hcl[hero][0] += hp_amount
#             print(f"{hero} healed for {hp_amount} HP!")
#         else:
#             print(f"{hero} healed for {100 - hcl[hero][0]} HP!")
#             hcl[hero][0] = 100
#
#     command = input()
#
# for key,value in hcl.items():
#     print(f"{key}\n  HP: {value[0]}\n  MP: {value[1]}")


import sys
from io import StringIO

input1 = """2
Solmyr 85 120
Kyrre 99 50
Heal - Solmyr - 10
Recharge - Solmyr - 50
TakeDamage - Kyrre - 66 - Orc
CastSpell - Kyrre - 15 - ViewEarth
End"""

input2 = """4
Adela 90 150
SirMullich 70 40
Ivor 1 111
Tyris 94 61
Heal - SirMullich - 50
Recharge - Adela - 100
CastSpell - Tyris - 1000 - Fireball
TakeDamage - Tyris - 99 - Fireball
TakeDamage - Ivor - 3 - Mosquito
End
"""

sys.stdin = StringIO(input2)

heroes = {}

n = int(input())
for i in range(n):
    name, hp, mp = input().split()
    heroes[name] = [int(hp),int(mp)]
# hero can have a maximum of 100 HP and 200 MP

command = input()
while not command == "End":
    command_split = command.split(" - ")

    action = command_split[0]
    hero_name = command_split[1]
    if action == "CastSpell":
        mp_needed = int(command_split[2])
        spell_name = command_split[3]
        if mp_needed <= heroes[hero_name][1]:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(command_split[2])
        attacker = command_split[3]
        if heroes[hero_name][0] - damage > 0:
            heroes[hero_name][0] -= damage

            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

    elif action == "Recharge":
        amount = int(command_split[2])
        if heroes[hero_name][1] + amount <= 200:
            heroes[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            add_mp = 200 - heroes[hero_name][1]
            heroes[hero_name][1] = 200
            print(f"{hero_name} recharged for {add_mp} MP!")

    elif action == "Heal":
        amount = int(command_split[2])
        if heroes[hero_name][0] + amount <= 100:
            heroes[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")
        else:
            add_hp = 100 - heroes[hero_name][0]
            heroes[hero_name][0] = 100
            print(f"{hero_name} healed for {add_hp} HP!")

    command = input()

for key,value in heroes.items():
    print(f"{key}\n  HP: {value[0]}\n  MP: {value[1]}")



























