# from math import pow      #Повдигане на степен
# number_of_snowball = int(input())
# max_value = 0
# max_snowball_weight = 0
# max_snowball_time = 0
# max_snowball_quality = 0
# for snowball in range(number_of_snowball):
#     snowball_weight = int(input())
#     snowball_time = int(input())
#     snowball_quality = int(input())
#     current_snowball_value = pow(snowball_weight/snowball_time, snowball_quality)
#     if current_snowball_value > max_value:
#         max_value = current_snowball_value
#         max_snowball_weight = snowball_weight
#         max_snowball_time = snowball_time
#         max_snowball_quality = snowball_quality
# print(f'{max_snowball_weight} : {max_snowball_time} = {max_value:.0f} ({max_snowball_quality})')


best_snowball_value = 0
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0
n = int(input())
for _ in range(n):

    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time} = {int(best_snowball_value)} ({best_snowball_quality})")




















