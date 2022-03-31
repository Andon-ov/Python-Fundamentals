# import sys
# from io import StringIO
#
# input1 = """#lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#"""
# input2 = """#po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@"""
# input3 = """@mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r"""
#
# sys.stdin = StringIO(input3)
# import re
#
# text = input()
# # regex = r"(@|#)([A-Za-z]{3,})\1"
# # regex = r"(@|#)(?P<word>[A-Za-z]{3,})\1"
# regex = r"(?P<separator>@|#)(?P<word>[A-Za-z]{3,})(?P=separator)(?P=separator)(?P<mirror_word>[A-Za-z]{3,})(?P=separator)"
#
# word_sum = 0
# mirror_words = []
# match = re.finditer(regex, text)
# for i in match:
#
#     word = i.group("word")
#     mirror_word = i.group("mirror_word")
#     if word == mirror_word[::-1]:
#         mirror_words.append(f"{word} <=> {mirror_word}")
#
#     word_sum += 1
#
# if not word_sum > 0:
#     print("No word pairs found!")
#
#     if not len(mirror_words) > 0:
#         print("No mirror words!")
#
# if word_sum > 0:
#     print(f"{word_sum} word pairs found!")
#
#     if len(mirror_words) > 0:
#         print("The mirror words are:")
#         print(", ".join(mirror_words))
#
#     elif not len(mirror_words) > 0:
#         print("No mirror words!")

import sys
from io import StringIO

input1 = """@mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r	
"""
input2 = """#po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@
"""
input3 = """#lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#"""

sys.stdin = StringIO(input3)

import re

regex = r"(#|@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
text = input()
match = re.findall(regex, text)

mirror_words = []
for i in match:
    if i[1] == i[2][::-1]:
        mirror_words.append(f"{i[1]} <=> {i[2]}")

if len(match) > 0:
    print(f"{len(match)} word pairs found!")

    if len(mirror_words) > 0:
        print(f"The mirror words are:")
        print(", ".join(mirror_words))

    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")
