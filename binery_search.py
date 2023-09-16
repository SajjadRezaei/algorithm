def search(list, target):
    low, heigh = 0, len(list) - 1

    while low <= heigh:
        mid = (heigh + low) // 2
        val = list[mid]
        if val == target:
            return mid
        elif val < target:
            low = mid + 1
        else:
            heigh = mid - 1
    return -1


print(search([2, 3, 4, 6, 12, 19, 20, 21], 4))
