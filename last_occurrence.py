"""
    last occurrence
        [2,2,2,3,3,4,4,5,5,7,8,9,9] 4 => 6
"""


def lastOccurrence(array, element):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if (array[mid] == element and mid == len(array) - 1) or \
                (array[mid] == element and array[mid] + 1 > element):
            return mid
        elif array[mid] <= element:
            low = mid + 1
        else:
            high = mid - 1
