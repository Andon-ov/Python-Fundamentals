n = int(input())
water_tank = 255
get_water = 0

for _ in range(n):
    liters_of_water = int(input())
    if water_tank - liters_of_water < 0:
        print(f'Insufficient capacity!')
        continue

    get_water += liters_of_water
    water_tank -= liters_of_water
print(get_water)
