from collections import Counter

s = 'leetcode'


def firstUniqueChar(s):
    counter = Counter(s)

    for idx, char in enumerate(s):
        if counter[char] == 1:
            return idx

    return -1


print(firstUniqueChar(s))
