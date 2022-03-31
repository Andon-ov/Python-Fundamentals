# # Взимаме си картите и колко пъти трябва да ги разбъркаме
# deck = input().split()
# number_of_shuffle = int(input())
# # Правим си лява и дясна половина на листа
# left_half = []
# right_half = []
# # Въртим цикъл с разбърквания за колкото са те
# for shuffles in range(number_of_shuffle):
#     # създаваме си временна променлива която след всяко завъртане сеиваме в deck
#     current_deck = []
#     # намираме средата на картите
#     half = int(len(deck)/2)
#     # обозначаваме на какво е равна лявата и дясната половина на листовете със слайсинг
#     left_half = deck[:half]
#     right_half = deck[half:]
#     # въртим цикъл от брояна половината карти
#     for card in range(half):
#         # взимаме карта от левия списък със индекса и и от десния и ги добавяме съм временната променлива - списък
#         current_deck.append(left_half[card])
#         current_deck.append(right_half[card])
#         # запазваме временната променлива с списъкът deck - за да може пак да го вземем и да го завъртим
#     deck = current_deck
# print(deck)


cards = input().split()
count = int(input())

half = len(cards) // 2

for i in range(count):
    temp = []
    half = len(cards) // 2

    left = cards[:half]
    right = cards[half:]

    for index in range(half):

        temp.append(left[index])
        temp.append(right[index])
    cards = temp
print(cards)






















