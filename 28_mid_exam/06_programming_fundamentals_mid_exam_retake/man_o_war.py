# import sys
# from io import StringIO
#
# input1 = """2>3>4>5>2
# 6>7>8>9>10>11
# 20
# Status
# Fire 2 3
# Defend 0 4 11
# Repair 3 18
# Retire"""
#
# sys.stdin = StringIO(input1)


def index_is_valid(index, list):
    if index in range(len(list)):
        return True
    else:
        return False


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
maximum_health_capacity = int(input())

command = input()
while not command == "Retire":
    command_split = command.split()
    action = command_split[0]

    if action == 'Fire':
        index = int(command_split[1])
        damage = int(command_split[2])
        if index_is_valid(index, warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                exit()

    elif action == 'Defend':
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        damage = int(command_split[3])
        if index_is_valid(start_index, pirate_ship) and index_is_valid(end_index, pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    exit()

    elif action == 'Repair':
        index = int(command_split[1])
        health = int(command_split[2])
        if index_is_valid(index, pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > maximum_health_capacity:
                pirate_ship[index] = maximum_health_capacity

    elif action == 'Status':
        need_repair = 0
        for i in range(len(pirate_ship)):
            if pirate_ship[i] < maximum_health_capacity * 0.2:
                need_repair +=1
        print(f"{need_repair} sections need repair.")

    command = input()
print(f"Pirate ship status: {sum(pirate_ship):.0f}\nWarship status: {sum(warship):.0f}")
