
number_of_electrons = int(input())
filled_shells = []
count = 1
while not number_of_electrons == 0:

    number = 2*(count**2)

    count += 1
    if number > number_of_electrons:
        filled_shells.append(number_of_electrons)
        break
    else:
        filled_shells.append(number)
        number_of_electrons -= number
print(filled_shells)
