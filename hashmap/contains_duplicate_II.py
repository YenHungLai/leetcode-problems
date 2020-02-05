nums = [1, 0, 1, 1]
k = 1


def containsNearbyDuplicate(nums, k):
    my_map = {}

    for idx, num in enumerate(nums):
        if num not in my_map:
            my_map[num] = idx
        else:
            if idx - my_map[num] <= k:
                return True

            my_map[num] = idx

    return False


print(containsNearbyDuplicate(nums, k))
