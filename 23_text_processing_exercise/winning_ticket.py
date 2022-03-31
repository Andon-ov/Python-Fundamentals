import sys
from io import StringIO

input1 = """validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$"""

sys.stdin = StringIO(input1)
winning_symbols = ['@', '#', '$', '^']


def jackpot(ticket):
    for symbol in winning_symbols:
        if symbol in ticket:
            if ticket.count(symbol) == 20:
                print(f'ticket "{ticket}" - {10}{symbol} Jackpot!')
                return True
    return False


def is_winning_ticket(ticket):
    left_side = ticket[:10]
    right_side = ticket[10:]
    for symbol in winning_symbols:
        if symbol * 6 in left_side and symbol * 6 in right_side:
            left_symbol_count = left_side.count(symbol)
            right_symbol_count = right_side.count(symbol)
            # Има грешка тук !!! Трябва да е 6тица
            number = min(left_symbol_count,right_symbol_count)
            print(f'ticket "{ticket}" - {number}{symbol}')
            return True
    return False


tickets = [x.strip() for x in input().split(", ")]

for ticket in tickets:

    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    if jackpot(ticket):
        continue

    if is_winning_ticket(ticket):
        continue

    if not is_winning_ticket(ticket):
        print(f'ticket "{ticket}" - no match')

# ToDO 90/100