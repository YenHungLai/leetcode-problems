T = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]


# def dailyTemperatures(T):
#     """Exceeds time limit but seems to work"""
#     stack = []
#     result = []
#     ptr = 0

#     while len(T) != 0:
#         if len(stack) == 0:
#             stack.append(T.pop(0))

#         while ptr <= len(T) - 1 and T[ptr] <= stack[0]:
#             stack.append(T[ptr])
#             ptr += 1

#         print(stack, T, ptr)
#         if ptr > len(T) - 1:
#             result.append(0)
#         else:
#             result.append(len(stack))

#         stack.clear()
#         ptr = 0

#     return result


# print(dailyTemperatures(T))


# def dailyTemperatures(T):
#     """Use pointers, time limit exceeded"""
#     if len(T) == 0:
#         return [0]

#     result, head, tail = [], 0, 1

#     while head <= len(T) - 1:
#         if tail <= len(T) - 1 and T[head] >= T[tail]:
#             tail += 1
#         else:
#             if tail > len(T) - 1:
#                 result.append(0)
#             else:
#                 result.append(tail - head)
#             head += 1
#             tail = head + 1

#         print(head, tail, result)

#     return result


# print(dailyTemperatures(T))
