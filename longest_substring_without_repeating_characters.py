from collections import defaultdict

s = "abcbda"


# def lengthOfLongestSubstring(s):
#     """Brute force, finding all substrings and their length"""
#     substring_map = defaultdict(int)
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             if len(set(s[i:j+1])) == len(s[i:j+1]):
#                 substring_map[s[i:j+1]] = len(s[i:j+1])

#     print(substring_map)
#     return max(substring_map.values())


# print(lengthOfLongestSubstring(s))


def lengthOfLongestSubstring(s):
    """Sliding window technique"""
    result = 0
    anchor = 0
    for idx in range(len(s)):
        if len(set(s[anchor:idx+1])) == len(s[anchor:idx+1]):
            if idx - anchor + 1 > result:
                result = idx - anchor + 1
        else:
            anchor += 1
        print(result, anchor, idx)

    return result


print(lengthOfLongestSubstring(s))
