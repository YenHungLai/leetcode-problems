nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


def rotate(nums, k):
    for _ in range(k):
        nums.insert(0, nums.pop())


rotate(nums, k)
print(nums)
