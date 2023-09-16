"""
    remove min
    [4,5,2,8,-2,5,1,9]
"""


def removeMin(stack):
    storageStack = []
    if len(stack) == 0:
        return stack

    min = stack.pop()
    stack.append(min)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= min:
            min = val
        storageStack.append(val)

    for i in range(len(storageStack)):
        val = storageStack.pop()
        if val != min:
            stack.append(val)
    return stack

print(removeMin([4,5,2,8,-2,5,1,9]))