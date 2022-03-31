# Write a function that calculates the total price of an order and returns it. The function should
# receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.
def total_price(product,quantities):
    if product == 'coffee':
        return quantities * 1.5
    elif product == 'coke':
        return quantities * 1.4
    elif product == 'water':
        return quantities
    elif product == 'snacks':
        return quantities * 2


products = input()
wanted_quantities =  float(input())
print(f'{total_price(products,wanted_quantities):.2f}')
