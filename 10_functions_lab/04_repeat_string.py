# Write a function that receives a string and a counter n. The function should return a new string
# – the result of repeating the old string n times. Print the result of the function. Try using lambda.
text = input()
counter = int(input())

result = lambda a, b: a * b
print(result(text, counter))
