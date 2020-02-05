# def isHappy(n):
#     s = []
#     while n != 1:
#         # Sum of all list elements.
#         n = sum([int(i) ** 2 for i in str(n)])
#         print(n)
#         if n in s:
#             return False
#         else:
#             s.append(n)

#     return True


def isHappy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum([int(i) ** 2 for i in str(n)])

    return n == 1


print(isHappy(19))
