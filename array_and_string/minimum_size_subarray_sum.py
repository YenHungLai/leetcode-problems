nums = [2, 3, 1, 2, 4, 3]
s = 7

# s = 213
# nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]


def minSubArrayLen(s, nums):
    head = 0
    val = 0
    ans = 0
    for idx in range(len(nums)):
        val += nums[idx]
        while val >= s:
            ans = min(ans, idx + 1 - head)
            val -= nums[head]
            head -= 1

    return ans


print(minSubArrayLen(s, nums))
