import sys
from io import StringIO

input1 = """163
16
67020
"""

sys.stdin = StringIO(input1)

from math import floor

per_day_for_one_worker = int(input())
workers = int(input())
other_fabric_for_30_days = int(input())
all_biscuits = 0

for i in range(1,30+1):
    if not i % 3 == 0:
        all_biscuits += (per_day_for_one_worker*workers)
    else:
        all_biscuits += floor((per_day_for_one_worker * workers) * 0.75)

my_vs_other_fabric = all_biscuits - other_fabric_for_30_days
my_vs_other_fabric_percentage = (my_vs_other_fabric/other_fabric_for_30_days)*100

print(f"You have produced {all_biscuits} biscuits for the past month.")
if all_biscuits > other_fabric_for_30_days:
    print(f"You produce {my_vs_other_fabric_percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {abs(my_vs_other_fabric_percentage):.2f} percent less biscuits.")
