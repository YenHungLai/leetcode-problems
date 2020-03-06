strs = ["flower", "flow", "flight"]


# def longestCommonPrefix(strs):
#     if '' in strs:
#         return ''

#     prefix = ''

#     for string in strs:
#         if prefix == '':
#             prefix = string
#         else:
#             head = 0
#             while head <= len(string) - 1 and head <= len(prefix) - 1 and prefix[head] == string[head]:
#                 head += 1

#             prefix = string[:head]
#             if prefix == '':
#                 return ''

#     return prefix


# print(longestCommonPrefix(strs))


# def longestCommonPrefix(strs):
#     """Binary search"""


# print(longestCommonPrefix(strs))
strs = ['aa', 'a']


def longestCommonPrefix(strs):
    """Search all strings at the same time WIP."""
    if '' in strs == 0 or len(strs) == 0:
        return ''

    prefix = ''
    ptr = 0

    for char in strs[0]:
        for i in range(1, len(strs)):
            if ptr > len(strs[i]) or char != strs[i][ptr]:
                return prefix

        prefix += char
        ptr += 1

    return prefix


print(longestCommonPrefix(strs))
