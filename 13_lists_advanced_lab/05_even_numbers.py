# Write a program that reads a single string with
#     numbers separated by comma and space ", ". Print the indices of all even numbers.
string = input().split(", ")
# с лист компрехеншан
int_as_str_1 = [int(i) for i in string]
# с мап
int_as_str = list(map(int, string))
# с лист компрехеншан
filter1 = [index for index in range(len(int_as_str_1)) if int_as_str[index] % 2 == 0]
# с филтър ламбда и мап
filter = list(map(lambda el: int_as_str.index(el), list(filter(lambda el: el % 2 == 0, int_as_str))))

print(filter1)
print(filter)
