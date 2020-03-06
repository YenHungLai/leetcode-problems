nums = [3, 6, 1, 0]


# def dominantIndex(nums):
#     largest = max(nums)
#     for num in nums:
#         if num * 2 > largest and num != largest:
#             return -1

#     return nums.index(largest)


# print(dominantIndex(nums))

def dominantIndex(self, nums):
    largest = max(nums)
    if all(m >= 2*x for x in nums if x != largest):
        return nums.index(largest)

    return -1
