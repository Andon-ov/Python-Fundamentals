def shoot_target (targets, curent_index, curent_value ):
    targets[curent_index] -= curent_value
    if targets[curent_index] <=0:
        targets.pop(curent_index)
        return targets


def add_target (targets, curent_index, curent_value ):
    targets.insert(curent_index, curent_value)
    return targets


def strike_target ():
    pass

sequence_of_targets = [int(i) for i in input().split()]
command = input()
while not command == "End":

    action, str_index, str_value = command.split()
    index = int(str_index)
    value = int(str_value)
    print(len(sequence_of_targets))

    if action == 'Shoot':
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets = shoot_target(sequence_of_targets, index , value)
            print(sequence_of_targets)

    elif action == 'Add':
        sequence_of_targets = add_target(sequence_of_targets, index, value)

    elif action == 'Strike':
        pass

    command = input()

print('|'.join([str(s) for s in sequence_of_targets]))