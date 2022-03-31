a = int(input())
b = int(input())
a,b = b, a
print('Before:')
print(f'a = {b}')
print(f'b = {a}')
print('After:')
print(f'a = {a}')
print(f'b = {b}')
