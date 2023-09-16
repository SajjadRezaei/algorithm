"""
    rotate
    rotate("hello",2) return "llohe"
"""


def rotate(s, k):
    doubleS = s + s
    print(doubleS[2])
    if k <= len(s):
        return doubleS[k:k + len(s)]
    else:
        return doubleS[k - len(s), k]


print(rotate("hello", 2))

