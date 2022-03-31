target_plunder_is_reached = False
days = int(input())
plunder_for_a_day = int(input())
expected_plunder = float(input())
plunder = 0
for day in range(1, days + 1):
    plunder += plunder_for_a_day
    if day % 3 == 0:
        plunder += plunder_for_a_day / 2
    if day % 5 == 0:
        plunder *= 0.7

if plunder >= expected_plunder:
    target_plunder_is_reached = True

if target_plunder_is_reached:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
else:
    print(f"Collected only {((plunder / expected_plunder) * 100):.2f}% of the plunder.")
