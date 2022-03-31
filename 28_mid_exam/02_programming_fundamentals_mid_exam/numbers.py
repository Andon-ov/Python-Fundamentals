#
# array = [int(i) for i in input().split()]
# final_list = []
#
# if len(array) <= 1:
#     print("No")
#
# avarage_number = sum(array)/len(array)
# for i in array:
#
#     if i > avarage_number:
#         final_list.append(i)
#         final_list.sort()
#         final_list = final_list[-1:-6:-1]
#
# print(' '.join([str(i) for i in final_list]))


numbers = [int(x) for x in input().split()]
greater = []
average_number = sum(numbers)/len(numbers)
for index in range(len(numbers)):
    if numbers[index] > average_number:
        greater.append(numbers[index])
        greater.sort(reverse=True)

if int(len(greater)) == 0:
    print('No')
    exit()

end_index = 5
if int(len(greater)) > end_index:
    greater = greater[:5]
print(' '.join([str(i) for i in greater]))

