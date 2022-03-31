# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format:
# "Found palindrome {number} times".
word = input().split()
searched_word = input()
palindromes = [i for i in word if i == i[::-1]]

print(palindromes)
print(f'Found palindrome {word.count(searched_word)} times')

# вариянт с входа от конзолата във компрехеншана
word = [i for i in input().split() if i == i[::-1]]
searched_word = input()

print(word)
print(f'Found palindrome {word.count(searched_word)} times')
