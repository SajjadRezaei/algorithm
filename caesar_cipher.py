from string import ascii_letters


def encript(string, key):
    alpha = ascii_letters
    result = ''

    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
    return result


def decrypt(string, key):
    key *= -1
    return encript(string, key)


def brute_force(string):
    alpha = ascii_letters
    key = 1
    brute_force_data = {}

    while key <= len(alpha):
        brute_force_data[key] = decrypt(string, key)
        key += 1
    return brute_force_data


print(brute_force('zhqqhk'))