list_of_gifts = input().split()
command = input()
while not command == "No Money":
    current_command = command.split()
    current_gift = current_command[1]

    if current_command[0] == 'OutOfStock':
        for index in range(len(list_of_gifts)):
            if list_of_gifts[index] == current_gift:
                list_of_gifts[index] = 'None'

    elif current_command[0] == 'Required':
        index = int(current_command[2])

        if 0 <= index < len(list_of_gifts):
            list_of_gifts[index] = current_gift

    elif current_command[0] == 'JustInCase':
        list_of_gifts[-1] = current_gift

    command = input()
print(' '.join([i for i in list_of_gifts if not i == 'None' ]))




gifts = input().split()
command = input()
while not command == "No Money":
    command_split = command.split()
    action = command_split[0]
    gift = command_split[1]
    # •	"OutOfStock {gift}"
    # o	Find the gifts with this name in your collection, if any, and change their values to "None".
    if action == 'OutOfStock':
        if gift in gifts:
            for i in range(len(gifts)):
                if gifts[i] == gift:
                    gifts[i] = 'None'

    # •	"Required {gift} {index}"
    # o	If the index is valid, replace the gift on the given index with the given gift.
    if action == 'Required':
        index = int(command_split[2])
        if 0 <= index <= len(gifts):
            gifts.pop(index)
            gifts.insert(index,gift)

    # •	"JustInCase {gift}"
    # o	Replace the value of your last gift with this one.
    if action == 'JustInCase':
        gifts.pop(len(gifts)-1)
        gifts.append(gift)

    command = input()

print(' '.join([i for i in gifts if not i == 'None']))












