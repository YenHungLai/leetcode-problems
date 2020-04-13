def mySqrt(x):
<<<<<<< Updated upstream
    if x < 2:
        return x

    # For x >= 2, square root 'a' is 0 < a < x/2
    left, right = 2, x // 2
    while left <= right:
        # Using numbers not indexes.
        pivot = left + (right - left) // 2
        num = pivot**2
        if num < x:
            left = pivot + 1
        elif num > x:
            right = pivot - 1
        else:
            return pivot

    return right
=======
    pass
>>>>>>> Stashed changes


print(mySqrt(8))
