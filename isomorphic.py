"""
      is isomorphic
         foo , bar   => False
         fowo , beee   => true

        {f:b, o:e,w:e} (b,e,e)
"""


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    dict = {}
    set_values = set()

    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in dict:
                return False
            dict[s[i]] = t[i]
            set_values.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False

    return dict, set_values


print(is_isomorphic('fow', 'bee'))
