nums = [1, 1, 0, 1, 1, 1]


def findMaxConsecutiveOnes(nums):
    count = result = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            if count > result:
                result = count
            count = 0

    if count > result:
        return count

    return result


print(findMaxConsecutiveOnes(nums))
