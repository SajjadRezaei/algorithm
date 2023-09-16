"""
    move zeros
    [False,1,0,1,2,0,1,3,"a"] => [False,1,1,2,1,3,"a",0,0]
"""


def moveZeros(seq):
    result = []
    zeros = 0
    for i in seq:
        if i == 0 and type(i) != bool:
            zeros += 1
        else:
            result.append(i)

    result.extend([0] * zeros)
    return result


print(moveZeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
