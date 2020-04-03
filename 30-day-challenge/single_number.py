inputs = [2,2,1]

# def singleNumber(nums):
    # """Use hashmap"""
    # my_map = {}
    # for num in nums:
        # if num in my_map:
            # my_map[num] = my_map[num] + 1
        # else:
            # my_map[num] = 1

    # return min(my_map, key=lambda k : my_map[k])

def singleNumber(nums):
    """2 * (a + b + c) - (a + a + b + b + c) = c"""
    return 2 * sum(set(nums)) - sum(nums)

print(singleNumber(inputs))
