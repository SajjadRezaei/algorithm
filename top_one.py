"""
 Top One
     [1,2,3,4,1,5,3,6,7,8,9] => [1,3]
"""


def topOne(arr):
    values = {}
    result = []

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    max_val = max(values.values())

    for i in values.keys():
        if values[i] == max_val:
            result.append(i)

    return result


print(topOne([1, 2, 3, 4, 1, 5, 3, 6, 7, 8, 9]))
