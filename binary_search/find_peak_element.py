nums = [1, 2, 3, 1]


def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        pivot = (left + right) // 2
        # If number on the right is bigger then it has the potential of being the peak.
        if nums[pivot] < nums[pivot + 1]:
            left = pivot + 1
        else:
            right = pivot

    return right


print(findPeakElement(nums))
