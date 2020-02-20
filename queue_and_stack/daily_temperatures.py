T = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]


def dailyTemperatures(T):
    """Use a stack to store all temperature less than target, then..."""
    stack = []
    result = []
    ptr = 0

    while len(T) != 0:
        if len(stack) == 0:
            stack.append(T.pop(0))

        if stack[0] < T[ptr]:
            result.append(len(stack))
            stack.clear()
            stack.append(T.pop(0))
            ptr = 0
        else:
            if ptr == len(T) - 1:
                result.append(0)
                result.append(0)
                stack.clear()
                stack.append(T.pop(0))
                ptr = 0
            else:
                stack.append(T[ptr])
                ptr += 1

    return result


print(dailyTemperatures(T))
