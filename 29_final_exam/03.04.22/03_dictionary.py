import sys
from io import StringIO

input1 = """programmer: an animal, which turns coffee into code | developer: a magician
fish | domino
Hand Over"""
input2 = """care: worry, anxiety, or concern | care: a state of mind in which one is troubled | face: the front part of the head, from the forehead to the chin
care | kitchen | flower
Test"""
input3 = """tackle: the equipment required for a task or sport | code: write code for a computer program | bit: a small piece, part, or quantity of something | tackle: make determined efforts to deal with a problem | bit: a short time or distance
bit | code | tackle
Test"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

my_dict = {}
text = input()
wanted_word = input().split(' | ')
command = input()
words = text.split(" | ")

for i in words:

    key_value = i.split(": ")

    key = key_value[0]
    value = key_value[1]

    if key not in my_dict:
        my_dict[key] = [value]

    else:
        my_dict[key].append(value)

if command == "Test":
    # samo dumite ot wanted
    for key, value in my_dict.items():
        if key in wanted_word:
            print(f"{key}:")
            for i in value:
                print(f" -{i}")


elif command == "Hand Over":
    for key in my_dict:
        print(key,end=' ')





