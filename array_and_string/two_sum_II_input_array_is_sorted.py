numbers = [2, 7, 11, 15]
target = 9


# def twoSum(numbers, target):
#     """Brute force, time limit exceeded"""
#     head = 0
#     tail = head + 1

#     while head != len(numbers) - 1:
#         while tail <= len(numbers) - 1:
#             if numbers[head] + numbers[tail] == target:
#                 return [head + 1, tail + 1]
#             tail += 1

#         head += 1
#         tail = head + 1


# print(twoSum(numbers, target))


def twoSum(numbers, target):
    """Two pointers"""
    head = 0
    tail = len(numbers) - 1

    while head < tail:
        if numbers[head] + numbers[tail] == target:
            return [head + 1, tail + 1]
        elif numbers[head] + numbers[tail] < target:
            head += 1
        else:
            tail -= 1


print(twoSum(numbers, target))
