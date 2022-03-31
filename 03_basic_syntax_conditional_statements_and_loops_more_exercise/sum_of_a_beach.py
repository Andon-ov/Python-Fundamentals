
# text = input().lower()
# words = ["sand", "water", "fish", "sun"]
# count = 0
# for i in words:
#     if i in text:
#         word_count_txt = text.count(i)
#         count += word_count_txt
# print(count)
#


words = ["sand", "water", "fish", "sun"]
text = input().lower()
count = 0
for word in words:
    if word in text:
        word_count_txt = text.count(word)
        count += word_count_txt

print(count)
