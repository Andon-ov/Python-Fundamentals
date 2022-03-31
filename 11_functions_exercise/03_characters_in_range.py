# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.

def according_to_the_ascii_code(a, b):
    collected_symbol = []
    for i in range(ord(first) + 1, ord(second)):
        collected_symbol.append(chr(i))
    return collected_symbol


first = input()
second = input()
print(' '.join(according_to_the_ascii_code(first, second)))
