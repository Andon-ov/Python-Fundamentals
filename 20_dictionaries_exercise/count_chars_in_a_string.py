from collections import Counter
# print(Counter(text))

# text = input()
# d = {}
# for x in text:
#     if not x == " ":
#         d[x] = d.get(x, 0) + 1
# for key,value in d.items():
#     print(f"{key} -> {value}")

text = input()
dict = {}

for char in text:
    if char == " ":
        continue
    if char not in dict:
        dict[char] = 0
    dict[char] += 1
for key, value in dict.items():
    print(f"{key} -> {value}")
