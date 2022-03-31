# You will receive three integer numbers.
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.
def sum_numbers(a, b):
    add_numbers = a + b
    return add_numbers


def subtract(ab, c):
    number = ab - c
    return number


first_number = int(input())
second_number = int(input())
three_number = int(input())

print(subtract(sum_numbers(first_number, second_number), three_number))
