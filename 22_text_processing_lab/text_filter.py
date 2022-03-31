# word = input().split(', ')
# string = input()
# for word in word:
#     string = string.replace(word, '*' * len(word))
# print(string)



import sys
from io import StringIO

input1 = """Linux, Windows
It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client"""

sys.stdin = StringIO(input1)

banned_word = input().split(', ')
text = input()
for word in banned_word:
    text = text.replace(word, '*' * len(word))

print(text)


















