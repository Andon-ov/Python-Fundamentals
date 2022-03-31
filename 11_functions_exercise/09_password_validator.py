#
# def must_be_between_6_and_10_characters(word):
#     if 6 <= len(word) <= 10:
#         return True
#     else:
#         print("Password must be between 6 and 10 characters")
#
#
# def must_consist_only_of_letters_and_digits(word):
#     letters_and_digits = word.isalnum()
#     if letters_and_digits:
#         return True
#     else:
#         print("Password must consist only of letters and digits")
#
#
# def must_have_at_least_2_digits(word):
#     count = 0
#     for i in range(len(word)):
#         if '0' <= word[i] <= '9':
#             count += 1
#     if count >= 2:
#         return True
#     else:
#         print("Password must have at least 2 digits")
#
#
# password = input()
# valid_or_not_valid = []
# valid_or_not_valid.append(must_be_between_6_and_10_characters(password))
# valid_or_not_valid.append(must_consist_only_of_letters_and_digits(password))
# valid_or_not_valid.append(must_have_at_least_2_digits(password))
#
# valid = all(valid_or_not_valid)
# if valid:
#     print("Password is valid")


def between_6_and_10_char(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        print('Password must be between 6 and 10 characters')


def only_letters_and_digits(password):
    if password.isalnum():
        return True
    else:
        print('Password must consist only of letters and digits')


def least_2_digits(password):
    digit = 0
    for i in password:

        if i.isdigit():
            digit += 1
    if digit >= 2:
        return True
    else:
        print('Password must have at least 2 digits')


word = input()

valid_or_not_valid = [between_6_and_10_char(word), only_letters_and_digits(word), least_2_digits(word)]

if all(valid_or_not_valid):
    print('Password is valid')