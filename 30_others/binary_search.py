def binary_search_slow(values, target):
    if not values:
        raise ValueError(f"{target} not in list")
    mid = len(values) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return mid + 1 + binary_search_slow(values[mid + 1:], target)
    else:
        return binary_search_slow(values[:mid], target)


# values = [1, 2, 3, 4, 5, 8, 9, 11, 23, 45]
# for val in values:
# print(val,binary_search_slow(values,val))
# print(binary_search_slow(values, 15))


def binary_search_fast(values, target, strat_index, end_index):
    if strat_index >= end_index:
        raise ValueError(f"{target} not in list")
    mid = (strat_index + end_index) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return binary_search_fast(values, target, mid + 1, end_index)
    else:
        return binary_search_fast(values, target, strat_index, mid)


values = [1, 2, 3, 4, 5, 8, 9, 11, 23, 45]
for val in values:
    print(val, binary_search_fast(values, val, 0, len(values)))
