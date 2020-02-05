import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


# def groupAnagrams(strs):
#     # TODO: How to use defaultdict, why pass in list?
#     ans = collections.defaultdict(list)
#     for s in strs:
#         # sorted(s) provides a unique key.
#         ans[tuple(sorted(s))].append(s)

#     return ans.values()

def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        # Initialize list with 26 elements.
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)

    return ans.values()


print(groupAnagrams(strs))
