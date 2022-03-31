# first_string = input()
# second_string = input()
# last_string = first_string
# for symbol_index in range(len(first_string)):
#     new_string = ''
#     for begining in range(0, symbol_index +1):
#         new_string += second_string[begining]
#     for ending in range(symbol_index +1,len(first_string)):
#         new_string += first_string[ending]
#     if new_string == last_string:
#         continue
#     print(new_string)
#     last_string = new_string

# first_string = input()
# second_string = input()
# new_string = ''
# for i in range(len(first_string)):
#     if first_string[i] != second_string[i]:
#         new_string += second_string[i]
#         print(second_string[:i+1]+first_string[i+1:])
#     elif first_string[i] == second_string[i]:
#         new_string += second_string[i]

first_string = input()
second_string = input()

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        print(second_string[:i+1]+first_string[i+1:])
