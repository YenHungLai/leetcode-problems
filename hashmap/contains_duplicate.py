nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def containsDuplicate(nums):
    mySet = set()
    for num in nums:
        if num not in mySet:
            mySet.add(num)
        else:
            return True

    return False


print(containsDuplicate(nums))
