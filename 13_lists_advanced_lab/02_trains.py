wagons = int(input())
trains = [0]*wagons
command = input()

while not command == "End":

    data = command.split()

    if data[0] == 'add':
        people = int(data[1])
        trains[-1] += people

    if data[0] == 'insert':
        index = int(data[1])
        people = int(data[2])
        trains[index] += people

    if data[0] == 'leave':
        index = int(data[1])
        people = int(data[2])
        trains[index] -= people
    command = input()

print(trains)

