
import sys
from io import StringIO

input1 = """C:\Projects\Data-Structures\LinkedList.cs"""

sys.stdin = StringIO(input1)


# reverse_text = []
# text = input()
# for i in range(len(text) - 1, -1, -1):
#     if text[i] == "\\":
#         break
#     reverse_text.append(text[i])
#
# new_text = (''.join(reverse_text[::-1]))
# new_text = new_text.split('.')
# file_name = new_text[0]
# file_extension = new_text[1]
#
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")


text = input().split("\\")
searched_text = text[-1].split(".")

print(f"File name: {searched_text[0]}")
print(f"File extension: {searched_text[1]}")

