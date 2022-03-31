import sys
from io import StringIO

input1 = """There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)"""

sys.stdin = StringIO(input1)

text = input()
for i in range(len(text)):
    if text[i] == ':':
        emoticon = text[i] + text[i + 1]
        print(emoticon)



# text = input()
# for i in range(len(text)):
#     if text[i] == ':':
#         emoticon = (text[i],text[i+1])
#         print(''.join(emoticon))
