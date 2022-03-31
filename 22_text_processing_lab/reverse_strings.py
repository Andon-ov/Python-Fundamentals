import sys
from io import StringIO

input1 = """helLo
Softuni
bottle
end"""

sys.stdin = StringIO(input1)
command = input()
while not command == "end":
    print(f"{command} = {command[::-1]}")

    command = input()
