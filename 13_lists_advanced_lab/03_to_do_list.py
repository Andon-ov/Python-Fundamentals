
to_do_list = [0]*10
command = input()
while not command == "End":

    index, task = command.split('-')

    index = int(index)-1
    to_do_list[index] = task
    command = input()
print([i for i in to_do_list if not i == 0])

