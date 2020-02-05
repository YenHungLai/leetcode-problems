nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


# def intersection(nums1, nums2):
#     result = [i for i in nums1 if i in nums2]
#     return list(set(result))

def intersection(nums1, nums2):
    n1 = set(nums1)
    n2 = set(nums2)

    # Use the built-in set intersection operator.
    return list(n1 & n2)


print(intersection(nums1, nums2))
