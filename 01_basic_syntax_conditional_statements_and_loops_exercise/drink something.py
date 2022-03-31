
age = int(input())
drink = ''
if 0 <= age <= 14:
    drink = 'drink toddy'
elif age <= 18:
    drink = 'drink coke'
elif age <= 21:
    drink = 'drink beer'
elif age > 21:
    drink = 'drink whisky'
print(drink)
