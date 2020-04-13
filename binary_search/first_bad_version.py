# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


# def firstBadVersion(n):
#     """Linear scan"""
#     for version in range(1, n + 1):
#         if isBadVersion(version):
#             return version


# print(firstBadVersion(5))


def firstBadVersion(n):
    """Binary search"""
    left, right = 1, n
    # Terminates when left == right
    while left < right:
        pivot = (left + right) // 2
        if isBadVersion(pivot):
            right = pivot
        else:
            left = pivot + 1

    return left


print(firstBadVersion(5))
