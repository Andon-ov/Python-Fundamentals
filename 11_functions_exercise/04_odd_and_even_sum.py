# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a
# given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.
# def sum_of_even_and_odd(num):


def sum_of_all_even_and_all_odd_digits(num):
    even_sum = 0
    odd_sum = 0
    for i in num:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return even_sum, odd_sum


number = input()
even, odd = sum_of_all_even_and_all_odd_digits(number)

print(f"Odd sum = {odd}, Even sum = {even}")
