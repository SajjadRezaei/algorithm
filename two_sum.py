"""
    tow sum
    [2,7,11,15],18 => [7,11]
"""


def twoSum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1
    while p1 < p2:
        s = numbers[p1] + numbers[p2]
        if s == target:
            return [numbers[p1], numbers[p2]], [p1, p2]
        elif s > target:
            p2 = p2 - 1
        else:
            p1 = p1 + 1


print(twoSum([2, 7, 11, 15], 18))
