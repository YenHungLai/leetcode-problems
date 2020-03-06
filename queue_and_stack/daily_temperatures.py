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


def dailyTemperatures(T):
    stack = []


print(dailyTemperatures(T))
