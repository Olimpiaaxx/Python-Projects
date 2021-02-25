def binary_search(ls, item):
    begin_index = 0
    end_index = len(ls) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = ls[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

ls_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = 4


print(binary_search(ls_a, item_a))
