# Write a program that prints part of the ASCII table characters on the console, separated by a single space.
# On the first line of input, you will receive the char index you should start with. On the second line
# - the index of the last character you should print.
first_number = int(input())
second_number = int(input())
for i in range(first_number, second_number+1):
    print(chr(i),end=' ')