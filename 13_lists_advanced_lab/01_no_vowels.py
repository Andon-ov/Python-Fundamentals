no_vowels = input()
string = [ i for i in no_vowels if i not in 'a''o''u''e''i']
print(''.join(string))

