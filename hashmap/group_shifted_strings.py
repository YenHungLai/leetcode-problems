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


# print(getCombo('abc'))


# def groupStrings(strings):
#     my_map = defaultdict(list)
#     for string in strings:
#         my_map[getCombo(string)].append(string)

#     return my_map.values()


# print(groupStrings(strings))

# Find offset between each letter and first letter.
# If two letters have the same offset then they can be shifted into each other.
def groupStrings(strings):
    my_map = defaultdict(list)
    for string in strings:
        offsets = []
        for letter in string:
            offset = ord(letter) - ord(string[0])
            if offset >= 0:
                offsets.append(offset)
            else:
                offsets.append(offset + 26)

        my_map[tuple(offsets)].append(string)

    return my_map


print(groupStrings(strings))
