from collections import Counter

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

# Brute force
# def intersect(nums1, nums2):
#     result = []

#     for num in nums1:
#         if num in nums2:
#             result.append(num)
#             nums2.remove(num)

#     return result


# def intersect(nums1, nums2):
#     c1 = Counter(nums1)
#     c2 = Counter(nums2)

#     print(c1)
#     print(c2)

#     result = []
#     for k, v in dict(c1).items():
#         if k in c2:
#             temp = min(v, c2[k])
#             for _ in range(temp):
#                 result.append(k)

#     return result


def intersect(nums1, nums2):
    cnt = Counter(nums1) if len(nums1) < len(nums2) else Counter(nums2)
    larger_arr = nums2 if len(nums2) > len(nums1) else nums1
    result = []

    print(cnt)

    for num in larger_arr:
        if num in cnt and cnt[num] != 0:
            result.append(num)
            cnt[num] = cnt[num] - 1

    return result


print(intersect(nums1, nums2))
