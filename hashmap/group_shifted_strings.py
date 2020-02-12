from collections import defaultdict

strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

# Brute force, get all combonations.


def getCombo(string):
    result = []
    for i in range(26):
        temp = ''
        for char in string:
            num = ord(char) + i
            if num <= 122:
                temp += chr(num)
            else:
                temp += chr(num - 26)

        result.append(temp)

    return tuple(sorted(result))


print(getCombo('abc'))


def groupStrings(strings):
    my_map = defaultdict(list)
    for string in strings:
        my_map[getCombo(string)].append(string)

    return my_map.values()


print(groupStrings(strings))
