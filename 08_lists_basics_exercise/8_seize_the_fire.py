# all_cells = input().split('#')
# water = int(input())
# effort = 0
# fire = 0
# cells_value = []
# for cell in all_cells:
#     type_of_fire,cell_value = cell.split(' = ')
#     if type_of_fire == 'High':
#         if not 81 <= int(cell_value) <= 125:
#             continue
#     elif type_of_fire == 'Medium':
#         if not 51 <= int(cell_value) <= 80:
#             continue
#     elif type_of_fire == 'Low':
#         if not 1 <= int(cell_value) <= 50:
#             continue
#     if water < int(cell_value):
#         continue
#     cells_value.append(cell_value)
#     water -= int(cell_value)
#     effort += int(cell_value) * 0.25
#     fire += int(cell_value)
# print(f'Cells:')
# for cell in cells_value:
#     print(f' - {cell}')
# print(f'Effort: {effort:.2f}')
# print(f'Total Fire: {fire}')


fire_cele = input().split('#')
water = int(input())

out_fire = []
for i in fire_cele:
    command = i.split(' = ')
    typeOfFire = command[0]
    valueOfCell = int(command[1])

    if typeOfFire == 'Low':
        if 1 <= valueOfCell <= 50:
            if water >= valueOfCell:
                water -= valueOfCell
                out_fire.append(valueOfCell)
    elif typeOfFire == 'Medium':
        if 51 <= valueOfCell <= 80:
                if water >= valueOfCell:
                    water -= valueOfCell
                    out_fire.append(valueOfCell)
    elif typeOfFire == 'High':
        if 81 <= valueOfCell <= 125:
                if water >= valueOfCell:
                    water -= valueOfCell
                    out_fire.append(valueOfCell)

print('Cells:')
for i in out_fire:
    print(f' - {i}')
print(f'Effort: {(sum(out_fire)/4):.2f}')
print(f'Total Fire: {sum(out_fire)}')













