import sys
from io import StringIO

input1 = """In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**"""
sys.stdin = StringIO(input1)


def multiplying_all_digits(text):
    cool_threshold = 1
    for char in text:
        if char.isdigit():
            cool_threshold *= int(char)
    return cool_threshold


import re

emojis_count = 0
emojis = []
text = input()
multiplying_all_digits(text)
# regex = r"(?<=(\*\*)|(::))([A-Z][a-z]{3,})(?=\1|\2)"
# regex = r"(?<=(\*\*)|(::))([A-Z][a-z]{2,})(?=\1|\2)"
regex = r"(\*\*|::)([A-Z][a-z]{2,})(\1|\2)"

match = re.findall(regex, text)
for i in match:

    letter_value = 0
    for letter in i[1]:
        letter_value += ord(letter)

    emojis_count += 1
    if letter_value >= int(multiplying_all_digits(text)):
        emojis.append(''.join(i))

print(f"Cool threshold: {multiplying_all_digits(text)}")
print(f"{emojis_count} emojis found in the text. The cool ones are:")
for emoji in emojis:
    print(emoji)

# import sys
# from io import StringIO
#
# input1 = """In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**"""
# input2 = """It is a long established fact that 1 a reader will be distracted by 9 the readable content of a page when looking at its layout. The point of using ::LoremIpsum:: is that it has a more-or-less normal 3 distribution of 8 letters, as opposed to using 'Content here, content 99 here', making it look like readable **English**."""
#
# sys.stdin = StringIO(input1)
# # sys.stdin = StringIO(input2)
#
#
#
# def digit_sum(text):
#     sum_digit = 1
#     for i in text:
#         if i.isdigit():
#             sum_digit *= int(i)
#     return sum_digit
#
#
# import re
# text = input()
# cool_emoji  = digit_sum(text)
# coolest_emoji = []
#
# regex = r"(\*\*|::)([A-Z][a-z]{2,})(\1)"
#
# matches = re.findall(regex,text)
#
# for i in matches:
#     is_cool_emoji = 0
#     for j in i[1]:
#         is_cool_emoji += ord(j)
#     if is_cool_emoji >= cool_emoji:
#         coolest_emoji.append(i)
#
#
# print(f"Cool threshold: {cool_emoji}")
# print(f"{len(matches)} emojis found in the text. The cool ones are:")
# for word in coolest_emoji:
#     print("".join(word))















