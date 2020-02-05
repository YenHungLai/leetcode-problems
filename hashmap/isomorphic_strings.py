s = 'paper'
t = 'title'


def isIsomorphic(s, t):
    if len(set(s)) != len(set(t)):
        return False

    str_map = {}

    for i, char in enumerate(s):
        if char not in str_map:
            str_map[char] = t[i]
        else:
            if str_map[char] != t[i]:
                return False

    return True


print(isIsomorphic(s, t))
