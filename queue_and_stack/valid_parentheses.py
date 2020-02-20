s = "()[]{}"


# def isValid(s):
#     stack = []

#     for char in s:
#         if len(stack) == 0:
#             stack.append(char)
#         elif char == '(' or char == '[' or char == '{':
#             stack.append(char)
#         else:
#             temp = stack.pop()
#             if char == ')' and temp != '(' or char == ']' and temp != '[' or char == '}' and temp != '{':
#                 return False

#     if len(stack) != 0:
#         return False

#     return True


# print(isValid(s))


def isValid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if len(stack) == 0 or char in pairs.values():
            stack.append(char)
        else:
            if stack.pop() != pairs[char]:
                return False

    return True


print(isValid(s))
