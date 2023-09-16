"""
    a1z26
        amir <==> [1,13,9,18]

        use ord() and chr func
"""


def encode(plain):
    return [ord(elm) - 91 for elm in plain]


def decode(encode):
    return "".join(chr(elm + 91) for elm in encode)


print(encode("sajjad"))
print(decode([115, 97, 106, 106, 97, 100]))
