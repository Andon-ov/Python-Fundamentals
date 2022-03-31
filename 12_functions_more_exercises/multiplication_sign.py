def positive_negative_or_zero(x, y, z):
    if ((x > 0 and y > 0 and z > 0)
            or (x < 0 and y < 0 and z > 0)
            or (x < 0 and y > 0 and z < 0)
            or (x > 0 and y < 0 and z < 0)):
        return 'positive'

    elif x == 0 or y == 0 or z == 0:
        return "zero"

    else:
        return 'negative'


a = int(input())
b = int(input())
c = int(input())

print(positive_negative_or_zero(a, b, c))
