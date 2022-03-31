key = int(input())
n = int(input())
for i in range(n):
    letter = input()
    decoder_letter = ord(letter) + key
    print(chr(decoder_letter),end='')