nums = [4, 5, 6, 7, 0, 1, 2
target = 0

# def search(nums, target):
#     temp = sorted(nums)
#     left, right = 0, len(temp) - 1
#     while left <= right:
#         pivot = (left + right) // 2
#         if temp[pivot] == target:
#             return nums.index(temp[pivot])
#         elif temp[pivot] < target:
#             left = pivot + 1
#         else:
#             right = pivot - 1

#     return -1

def find_rotate_index(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] > nums[pivot + 1]:
            return pivot + 1
        else:
            if nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1

def search(nums, target):
    """Use binary search to find the smallest element and then use binary search on either left or right side of that element."""
    print(find_rotate_index(nums))


print(search(nums, target))
