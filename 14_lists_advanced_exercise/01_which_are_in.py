# string = input().split(', ')
# searched_text = ''.join(input())
# final_text = []
# for i in string:
#     if i in searched_text:
#         final_text.append(i)
# print(final_text)


searched_words = input().split(', ')
strings = input().split(', ')
new_string = []
for j in searched_words:
    for i in strings:
        if j in i and j not in new_string:
            new_string.append(j)

print(new_string)















