# def variant_one(team, side, user):
#     if side not in team:
#         team[side] = []
#         team[side].append(user)
#     return team
#
#
# def variant_two(team, side, user):
#     if side not in team:
#         team[side] = []
#         team[side].append(user)
#     else:
#         for key, value in teams.items():
#             for i in value:
#                 if i == user:
#                     value.remove(i)
#
#         team[side].append(user)
#         print(f"{user} joins the {side} side!")
#     return team



def add_user(team, side, user):
    for key, value in teams.items():
        if user in value:
            return team
    if side not in team:
        team[side] = [user]
    else:
        team[side].append(user)
    return team
    # - 30 точки от тук


def change_side(team, side, user):
    for key, value in teams.items():
        if user in value:
            team[key].remove(user)
            return add_user(team, side, user)
    return add_user(team, side, user)
    # - 30 точки от тук


teams = {}
command = input()
while not command == "Lumpawaroo":

    if "|" in command:
        force_side, force_user = command.split(" | ")
        add_user(teams, force_side, force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        change_side(teams, force_side, force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for key, value in teams.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for i in value:
            print(f"! {i}")
