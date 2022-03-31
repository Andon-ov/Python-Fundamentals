import math
# Python code to demonstrate naive method
# to compute factorial
n = 9
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"The factorial of 20 is {fact} ")

# math function
print(math.factorial(n))


# Recursive factorial
def factorial(number):
    if number == 1:
        return 1
    return n * factorial(number - 1)


n = 5
print(factorial(n))
