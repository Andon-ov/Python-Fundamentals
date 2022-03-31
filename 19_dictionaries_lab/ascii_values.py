# chars = input().split(', ')
# print({char: ord(char) for char in chars})


char = input().split(", ")
values = {}
for i in char:
    key = i
    value = ord(i)
    values[key] = value

print(values)


















