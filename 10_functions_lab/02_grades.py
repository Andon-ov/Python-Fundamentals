def found_grade(number):
    if 2 <= number <= 2.99:
        return "Fail"
    elif 3 <= number <= 3.49:
        return "Poor"
    elif 3.5 <= number <= 4.49:
        return "Good"
    elif 4.5 <= number <= 5.49:
        return "Very Good"
    elif 5.5 <= number <= 6:
        return "Excellent"


grade = float(input())
print(found_grade(grade))






