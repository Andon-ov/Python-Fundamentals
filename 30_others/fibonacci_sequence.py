# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1


# yield
def fin(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


ln = int(input('How long? '))
print(list(fin(ln)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]


# Recursive Fibonacci
def fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


n = 15
print(fibonacci(n))