nums = [3, 2, 2, 3]
val = 3


def removeElement(nums, val):
    ptr = 0
    for idx in range(len(nums)):
        if nums[idx] != val:
            nums[ptr] = nums[idx]
            ptr += 1

    return ptr


print(removeElement(nums, val))
print(nums)
