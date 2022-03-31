searched_string = input()
word = input()

while searched_string in word:
    word = word.replace(searched_string, '')
print(word)


# searched_string = input()
# word = input()
#
# new_word = ''
# for i in word:
#     if not i in searched_string:
#         new_word += i
# print(new_word)




















