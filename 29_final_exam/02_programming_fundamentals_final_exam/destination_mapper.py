import sys
from io import StringIO

input1 = """=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i="""
input2 = """ThisIs some InvalidInput"""
input3 = """"""

sys.stdin = StringIO(input2)

import re

destinations = []
travel_points = 0

regex = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
text = input()
match = re.findall(regex, text)
for i in match:
    travel_points += len(i[1])
    destinations.append(i[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")






