# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

number = [int(i) for i in input().split()]
even_numbers = list(filter(lambda a: a % 2 == 0, number))
print(even_numbers)
