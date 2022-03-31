commands = input()
coffe = 0
extra_sleep = False
while commands != "END":

    if commands in ("DOG", "CAT", "MOVIE","CODING"):
        coffe += 2

    elif commands in ("dog", "cat", "coding", "movie"):
        coffe += 1

    if coffe > 5:
        extra_sleep = True

    commands = input()
if extra_sleep:
    print('You need extra sleep')
else:
    print(coffe)


lower = ['coding', 'movie', 'dog', 'cat']
upper = ['CODING', 'MOVIE', 'DOG', 'CAT']

extra_sleep = False
number_of_coffees = 0
command = input()
while not command == "END":

    if command in lower:
        number_of_coffees += 1

    elif command in upper:
        number_of_coffees +=2

    if number_of_coffees > 5:
        extra_sleep = True
        break

    command = input()
if extra_sleep:
    print('You need extra sleep')

else:
    print(number_of_coffees)
