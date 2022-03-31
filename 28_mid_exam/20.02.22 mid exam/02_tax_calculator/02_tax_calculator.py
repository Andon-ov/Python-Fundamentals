import sys
from io import StringIO

input1 = """family 3 7210>>van 4 2345>>heavyDuty 9 31000>>sports 4 7410"""

sys.stdin = StringIO(input1)

string = input().split('>>')
taxes = 0
for i in string:
    command_split = i.split()
    type_car = command_split[0]
    years = int(command_split[1])
    km = int(command_split[2])

    if type_car == "family": # km / km ot uslowieto * 12 + (taksa ot uslovieto 50 - godinite)*5
        tax = ((km // 3000)) * 12 + (50 - (years * 5))
        print(f"A {type_car} car will pay {tax:.2f} euros in taxes.")
        taxes += tax

    elif type_car == "heavyDuty":
        tax = ((km // 9000)) * 14 + (80 - (years * 8))
        print(f"A {type_car} car will pay {tax:.2f} euros in taxes.")
        taxes += tax

    elif type_car == "sports":
        tax = ((km // 2000)) * 18 + (100 - (years * 9))
        print(f"A {type_car} car will pay {tax:.2f} euros in taxes.")
        taxes += tax

    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {taxes:.2f} euros in taxes.")
