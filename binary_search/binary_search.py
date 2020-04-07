"""
- Collection needs to be sorted. 
- Divide search space in half every iteration.
"""
nums = [-1, 0, 3, 5, 9, 12]
target = 9


def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        else:
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

    return -1


print(search(nums, target))
