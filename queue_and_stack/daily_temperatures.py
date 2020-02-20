T = [73, 74, 75, 71, 69, 72, 76, 73]


def dailyTemperatures(T):
    stack = []
    result = []

    while len(T) != 0:
        if len(stack) == 0:
            stack.append(T.pop(0))

        temp = T.pop(0)
        if temp > stack[0]:
            result.append(len(stack))
            stack.clear()
        else:
            stack.append(temp)

        print(result)

    return result


print(dailyTemperatures(T))
