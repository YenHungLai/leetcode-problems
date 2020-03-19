nums = [1, 4, 3, 2]


def arrayPairSum(nums):
    sum = 0
    nums = sorted(nums)
    for idx in range(0, len(nums), 2):
        sum += nums[idx]

    return sum


print(arrayPairSum(nums))
