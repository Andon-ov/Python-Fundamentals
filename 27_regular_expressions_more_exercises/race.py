import sys
from io import StringIO

input1 = """George, Peter, Bill, Tom
G4e@55or%6g6!68e!!@
R1@!3a$y4456@
B5@i@#123ll
G@e54o$r6ge#
7P%et^#e5346r
T$o553m&6
end of race"""

sys.stdin = StringIO(input1)

participants = {key: 0 for key in input().split(", ")}

data = input()
while not data == "end of race":

    name = ''
    distance = 0
    for char in data:
        if char.isalpha():
            name += char
        elif char.isdigit():
            distance += int(char)
    if name in participants.keys():
        participants[name] += distance

    data = input()
participants = list(sorted(participants.items(), key=lambda item: -item[1]))

print(f"1st place: {participants[0][0]}")
print(f"2nd place: {participants[1][0]}")
print(f"3rd place: {participants[2][0]}")
