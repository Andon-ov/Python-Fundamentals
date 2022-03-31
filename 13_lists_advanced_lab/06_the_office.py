people = input().split()
factor = int(input())
# int_people = list(map(int,people)) # с мап
generally_happy = [int(i)*factor for i in people]
# generally_happy = list(map(lambda i: i * factor ,int_people)) # с мап и лампда
average = sum(generally_happy) / len(generally_happy)
happy_count = [i for i in generally_happy if i > average]
# happy_count = list(filter(lambda i: i > average, generally_happy ))# с филтър и лампда

if len(happy_count) >= len(generally_happy) // 2:
    print(f"Score: {len(happy_count)}/{len(generally_happy)}. Employees are happy!")

else:
    print(f"Score: {len(happy_count)}/{len(generally_happy)}. Employees are not happy!")
