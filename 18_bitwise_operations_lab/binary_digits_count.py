number_to_binary = int(input())
searchet_number = int(input())
# binary_number_list = []
count = 0
while number_to_binary != 0:
    leftover = number_to_binary % 2
    # binary_number_list.append(leftover)

    if leftover == searchet_number:
        count += 1
    number_to_binary = number_to_binary //2

# binary_number = binary_number_list[::-1]
print(count)
# print(binary_number)



