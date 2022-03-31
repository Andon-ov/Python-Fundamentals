text = input()
a_list = []
for index, value in enumerate(text):
    if 65 <= ord(value) <= 90:
        a_list.append(index)
print(a_list)