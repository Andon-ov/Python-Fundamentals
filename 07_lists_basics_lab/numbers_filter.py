n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

criterion = input()
filtered = []
is_even = criterion == 'even'
is_odd = criterion == 'odd'
is_negative = criterion == 'negative'
is_positive = criterion == 'positive'
for num in numbers:
    if (is_even and num % 2 == 0)\
        or (is_odd and num % 2 != 0)\
        or ( is_negative and num < 0)\
        or (is_positive and num >= 0):
        filtered.append(num)
print(filtered)



