# names = input().split(', ')
# names = sorted(names) # първо сортираме азбучно
# names = sorted(names, key=lambda x: -len(x)) # После по дължина на имената
# print(names)

names1 = input().split(', ')
names1 = sorted(names1, key=lambda x: (-len(x),x)) # Двете в едно
print(names1)