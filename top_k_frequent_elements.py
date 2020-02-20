from collections import defaultdict
import heapq

nums = [3, 0, 1, 0]
k = 1


# def topKFrequent(nums, k):
#     """Brute force"""
#     my_map = defaultdict(int)
#     result = []
#     for num in nums:
#         my_map[num] += 1

#     print(my_map)

#     for _ in range(k):
#         temp = max(my_map, key=lambda key: my_map[key])
#         my_map.pop(temp)
#         result.append(temp)

#     return result


# print(topKFrequent(nums, k))


def topKFrequent(nums, k):
    my_map = defaultdict(int)
    result = []
    for num in nums:
        my_map[num] += 1

    print(my_map)

    sortedList = sorted(my_map, key=lambda x: my_map[k])
    print(sortedList)

    for _ in range(k):
        result.append(sortedList.pop(0))

    return result


print(topKFrequent(nums, k))
