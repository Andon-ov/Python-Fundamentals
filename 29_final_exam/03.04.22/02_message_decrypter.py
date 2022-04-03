import sys
from io import StringIO

input1 = """4
$Request$: [73]|[115]|[105]|
%Taggy$: [73]|[73]|[73]|
%Taggy%: [118]|[97]|[108]|
$Request$: [73]|[115]|[105]|[32]|[75]|"""
input2 = """3
This shouldnt be valid%Taggy%: [118]|[97]|[108]|
$tAGged$: [97][97][97]|
$Request$: [73]|[115]|[105]|true"""
input3 = """"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


import re

# regex = r"^(\$|%)([A-Z][a-z]{2,})\1:\s\[\d*\]\|\[\d*\]\|\[\d*\]\|$"
regex = r"^(\$|%)([A-Z][a-z]{2,})\1:\s\[([\d]*)\]\|\[([\d]*)\]\|\[([\d]*)\]\|$"
valid_message = {}
n = int(input())
for _ in range(n):
    text = input()

    matches = re.findall(regex, text)
    if not matches:
        print("Valid message not found!")
    else:

        word = []
        for i in matches:
            valid_message[i[1]] = [chr(int(i[2])), chr(int(i[3])), chr(int(i[4]))]
            one = chr(int(i[2]))
            two = chr(int(i[3]))
            three = chr(int(i[4]))
            word.append(one)
            word.append(two)
            word.append(three)
            print(f"{i[1]}: {''.join(word)}")

