def center_point(x, y, x1, y1):
    result = abs(x) + abs(y)
    result_1 = abs(x1) + abs(y1)

    if result < result_1:

        return f"({x:.0f}, {y:.0f})"
    else:
        return f"({x1:.0f}, {y1:.0f})"


a = float(input())
b = float(input())
a1 = float(input())
b1 = float(input())

print(center_point(a, b, a1, b1))


