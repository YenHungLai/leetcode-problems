nums = [1, 7, 3, 6, 5, 6]


# def pivotIndex(nums):
#     total = sum(nums)
#     for idx in range(len(nums)):
#         left = sum(nums[0:idx])
#         if left == sums - left - nums[idx]:
#             return idx

#     return -1


# print(pivotIndex(nums))

def pivotIndex(nums):
    total = sum(nums)
    left = 0

    for idx, val in enumerate(nums):
        if left == total - left - nums[idx]:
            return idx

        left += nums[idx]

    return -1


print(pivotIndex(nums))
