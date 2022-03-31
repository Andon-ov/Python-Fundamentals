# country = input().split(", ")
# capitals = input().split(", ")
# dict_capitals = dict(zip(country, capitals))
#
# for key,value in dict_capitals.items():
#     print(f"{key} -> {value}")


country = input().split(", ")
capital = input().split(", ")

country_capital = {country[i]: capital[i] for i in range(len(country))}
for key, value in country_capital.items():
    print(f"{key} -> {value}")
