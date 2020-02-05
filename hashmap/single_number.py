nums = [4, 1, 2, 1, 2, ]


# def singleNumber(nums):
#     mySet = []

#     for num in nums:
#         if num not in mySet:
#             mySet.append(num)
#         else:
#             mySet.remove(num)

#     return mySet.pop()

def singleNumber(nums):
    myMap = {}

    for num in nums:
        if num not in myMap:
            myMap[num] = 1
        else:
            myMap.pop(num)

    return myMap.popitem()[0]


print(singleNumber(nums))
