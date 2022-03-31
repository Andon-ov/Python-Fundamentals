numbers = input().split()   # взимаме поредица от числа и ги сплитваме(вкарваме в лист като отделни числа)
all_numbers = []            # име на листа
for index in range(len(numbers)):      # фор цикъл за цялата дължина на числата
    all_number = - int(numbers[index]) # променлива в която донавяме -инт (обръщаме числото)
    all_numbers.append(all_number)     # добавяме променливата към списака
print(all_numbers)


nums = [-int(number) for number in input().split()]
print(nums)

all_numbers = [int(i)*-1 for i in input().split()]
print(all_numbers)





































