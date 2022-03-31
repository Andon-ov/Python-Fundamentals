#
# miner_task = {}
# while True:
#     item = input()
#
#     if item == 'stop':
#         break
#
#     number = int(input())
#
#     if item in miner_task:
#         miner_task[item] += int(number)
#     else:
#         miner_task[item] = int(number)
#
# for resource, quantity in miner_task.items():
#     print(f"{resource} -> {quantity}")
#
#

miner = {}
while True:

    command = input()

    if command == 'stop':
        break
    number = input()

    if command not in miner:
        miner[command] = 0
    miner[command] += int(number)

for resource, quantity in miner.items():
    print(f"{resource} -> {quantity}")


