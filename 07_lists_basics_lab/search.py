strings = []
sorted_string = []
n = int(input())
word = input()

for i in range(n):
    string = input()
    strings.append(string)

    if word in string:
        sorted_string.append(string)
print(strings)
print(sorted_string)