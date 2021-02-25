def quick_sort(ls):
    length = len(ls)
    if length <= 1:
        return ls
    else:
        pivot = ls.pop()

    items_greater = []
    items_lower = []

    for item in ls:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([1, 3, 4, 5, 5, 7, 9]))
