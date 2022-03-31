
# Всеки ден морското свинче изяжда 300 гр. храна.
# Всеки втори ден Мери първо храни домашния любимец, след което му дава определено количество сено, равно на 5% от останалата храна.
# На всеки трети ден Merry поставя Puppy покривало с количество 1/3 от теглото му.

# Изчислете дали количеството храна, сено и покривка ще ви стигнат за един месец.
# Ако на Merry свърши храната, сеното или покривалото, спрете програмата!
# def is_fine(food, hay, cover):
#     if food <= 0 or hay <= 0 or cover <= 0:
#         return False
#     return True
#
# is_enough = True
# food_in_kg = float(input())
# hay_in_kg = float(input())
# cover_in_kg = float(input())
# guinea_in_kg = float(input())
#
# food_in_gr = food_in_kg * 1000
# hay_in_gr = hay_in_kg * 1000
# cover_in_gr = cover_in_kg * 1000
# guinea_in_gr = guinea_in_kg * 1000
#
# # if food_in_gr <=0 or hay_in_gr <=0 or cover_in_gr <=0:
# #     print("Merry must go to the pet store!")
# #     exit()
# for i in range(1,30+1):
#     if is_fine(food_in_gr,hay_in_gr,cover_in_gr):
#         food_in_gr -= 300
#     else:
#         is_enough = False
#         break
#     if i % 2 == 0:
#         if is_fine(food_in_gr, hay_in_gr, cover_in_gr):
#             hay_in_gr -= food_in_gr * 0.05
#         else:
#             is_enough = False
#             break
#     if i % 3 == 0:
#         if is_fine(food_in_gr, hay_in_gr, cover_in_gr):
#             cover_in_gr -= guinea_in_gr /3
#         else:
#             is_enough = False
#             break
# if is_enough:
#     print(f"Everything is fine! Puppy is happy! Food: {(food_in_gr/1000):.2f}, Hay: {(hay_in_gr/1000):.2f}, Cover: {(cover_in_gr/1000):.2f}.")
# else:
#     print("Merry must go to the pet store!")


food_in_kg = float(input())
hay_in_kg = float(input())
cover_in_kg = float(input())
pig_in_kg = float(input())
cover = pig_in_kg * (1.0 / 3)

for i in range(1, 30 + 1):

    food_in_kg -= 0.3
    amount_of_hay = food_in_kg * 0.05
    if i % 2 == 0:
        hay_in_kg -= amount_of_hay
    if i % 3 == 0:
        cover_in_kg -= cover

if food_in_kg > 0 and hay_in_kg > 0 and cover_in_kg > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_kg:.2f}, Hay: {hay_in_kg:.2f}, Cover: {cover_in_kg:.2f}.")
else:
    print("Merry must go to the pet store!")

































