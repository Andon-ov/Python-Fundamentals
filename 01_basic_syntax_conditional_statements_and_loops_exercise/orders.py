n = int(input())
sum = 0
for _ in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())
    total = price*days*capsules
    print(f"The price for the coffee is: ${total:.2f}")
    sum += total
print(f"Total: ${sum:.2f}")