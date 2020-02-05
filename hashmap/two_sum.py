nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    result = {}

    for i in range(len(nums)):
        if target - nums[i] not in result:
            result[nums[i]] = i
        else:
            return [i, result.get(target - nums[i])]


print(twoSum(nums, target))
