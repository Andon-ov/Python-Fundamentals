def replacement_character_code(word: str):
    ch_code_str = ''
    new_word = []

    for ch in word:
        if ch.isnumeric():
            ch_code_str += ch
        else:
            new_word.append(ch)
    ch_at_beginning = chr(int(ch_code_str))
    new_word.insert(0, ch_at_beginning)
    return new_word


def decipher_word(word: str):
    new_word = replacement_character_code(word)
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    return ''.join(new_word)


words = input().split()
deciphered_word = [decipher_word(word) for word in words]
print(' '.join(deciphered_word))


# string = input().split()
# text = []
#
# for i in string:
#     digit = ''
#     word = ''
#     new_word = ''
#     last_word = ''
#     for j in i:
#
#         if j.isdigit():
#             digit += j
#         else:
#             word += j
#     for c in range(len(word)):
#         if int(len(word)) > 1:
#
#             if not c == 0 and not c == len(word) - 1:
#                 new_word += word[c]
#
#             last_word = word[-1] + new_word + word[0]
#
#         elif int(len(word)) <= 1:
#             last_word = word[0]
#
#     text.append(chr(int(digit)) + last_word)
#
# print(' '.join([x for x in text]))
