def mySqrt(x):
    nums = [i for i in range(x)]
    left, right = 0, len(x) - 1
    while left <= right:
        pivot = (left + right) // 2


print(mySqrt(4))
