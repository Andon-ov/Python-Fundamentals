
# factor = int(input())
# count = int(input())
# list = []
# for i in range(1, count+1):
#     list.append(i * factor)
# print(list)


# factor = int(input())
# count = int(input())
# multiples_list = [nums * factor for nums in range(count+1)]
# print(multiples_list)


# factor = int(input())
# count = int(input())
# multiples = []
# for i in range(factor, (factor * count) + 1, factor):
#     print(i)


factor = int(input())
count = int(input())
multiples = [i for i in range(factor, (factor * count) + 1, factor)]
print(multiples)